from fastapi import FastAPI, HTTPException
import uvicorn
import pymongo
import os
from pydantic import BaseModel
from models import User
import hashlib

app = FastAPI()

DB_USER = os.environ['KICKIN_DB_USER']
DB_PASSWORD = os.environ['KICKIN_DB_PASSWORD']

client = pymongo.MongoClient(
    f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.4cnae.mongodb.net/app?retryWrites=true&w=majority'
)
db = client['app']


@app.get('/')
def hello():
    return {'message': 'Hello, World!'}


class ManagerCredentials(BaseModel):
    login: str
    password: str


@app.post('/manager_sign_up', response_model=User)
def manager_sign_up(data: ManagerCredentials):
    # TODO: handle if user exists
    password_hash = hashlib.sha256(data.password.encode('ascii')).hexdigest()
    user = User.parse_obj(
        {
            'login': data.login,
            'password_hash': password_hash,
            'role': 'manager'
        })

    obj_id = db.users.insert_one(user.dict()).inserted_id
    return db.users.find_one({'_id': obj_id})


@app.post('/manager_login', response_model=User)
def manager_login(data: ManagerCredentials):
    password_hash = hashlib.sha256(data.password.encode('ascii')).hexdigest()
    user = User.parse_obj(db.users.find_one({'login': data.login}))

    if user.password_hash == password_hash:
        return user
    raise HTTPException(status_code=401, detail='wrong credentials')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
