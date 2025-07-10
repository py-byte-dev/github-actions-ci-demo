from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/random-number")
def get_random_text():
    return {"result": True, "number": random.randint(1, 100)}


