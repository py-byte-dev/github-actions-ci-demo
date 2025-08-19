from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/random-number")
def get_random_text():
    return {"result": True, "number": random.randint(1, 100)}


@app.get("/random-text")
def get_random_text():
    return {"result": True, "text": random.randint(1, 100)}


@app.get("/random-number-text")
def get_random_text():
    return {"result": True, "number": random.randint(1, 100)}


@app.get("/random-text-text")
def get_random_text():
    return {"result": True, "text": random.randint(1, 100)}


@app.get("/random-number-text-text")
def get_random_text():
    return {"result": True, "number": random.randint(1, 100)}
