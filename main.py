from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()


@app.get('/')
def hello():
    return {'message': 'Hello, World!'}


if __name__ == "__main__":
    port = os.environ.get('PORT')
    uvicorn.run(app, host="0.0.0.0", port=port if port else 8000)
