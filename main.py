from fastapi import FastAPI
import uvicorn
import pymongo
import os

app = FastAPI()

DB_USER = os.environ['KICKIN_DB_USER']
DB_PASSWORD = os.environ['KICKIN_DB_PASSWORD']

client = pymongo.MongoClient(
    f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.4cnae.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
)

@app.get('/')
def hello():
    return {'message': 'Hello, World!'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
