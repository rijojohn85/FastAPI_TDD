from fastapi import FastAPI
from typing import Dict

app: FastAPI = FastAPI()


@app.get("/")
async def root()->Dict:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str)->Dict:
    return {"message": f"Hello {name}"}
