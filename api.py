from typing import Optional
from fastapi import FastAPI, Path

app = FastAPI()

todos = [
    {
        'id': 1,
        'name': 'Learn Python',
    },
    {
        'id': 2,
        'name': 'Learn FastAPI',
    }
]


@app.get("/")
def hello_world():
    return {"message": "API running"}


@app.get("/todos")
def get_all():
    return todos
