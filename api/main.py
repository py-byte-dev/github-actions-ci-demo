from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/random-text")
def get_random_text():
    return {"result": "ok", "number": random.randint(1, 100)}
