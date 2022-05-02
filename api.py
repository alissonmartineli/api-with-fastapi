from typing import Optional
from fastapi import FastAPI, Path, HTTPException

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
def get_all(name: Optional[str] = None):

    if not name:
        return todos

    return list(filter(lambda x: name in x["name"], todos))


@app.get("/todos/{id}")
def get_by_id(id: int = Path(None, description="The id of the todo you want to view")):

    search = list(filter(lambda x: x["id"] == id, todos))

    if search == []:
        raise HTTPException(status_code=404, detail="Todo not found")

    return search[0]
