from fastapi import APIRouter
from models.todo import TodoIn, TodoOut

router = APIRouter(prefix="/todos")

@router.get("/", response_model=list[TodoOut])
async def read_todos():
    return {"msg": "Get all todos."}

@router.post("/", response_model=TodoOut)
async def create_todo(todo: TodoIn):
    return todo

@router.get("/{id}", response_model=TodoOut)
async def read_todo(id: int):
    return {"msg": f"Get todo at id {id}."}

@router.put("/{id}", response_model=TodoOut)
async def update_todo(id: int, todo: TodoIn):
    return {"msg": f"Update todo at id {id}."}

@router.delete("/{id}")
async def delete_todo(id: int):
    return {"msg": f"Delete todo at {id}."}
