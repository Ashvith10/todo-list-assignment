from fastapi import APIRouter

router = APIRouter(prefix="/todos")

@router.get("/")
async def read_todos():
    return {"msg": "Get all todos."}

@router.post("/")
async def create_todo():
    return {"msg": "Create a todo."}

@router.get("/{id}")
async def read_todo(id: int):
    return {"msg": f"Get todo at id {id}."}

@router.put("/{id}")
async def update_todo(id: int):
    return {"msg": f"Update todo at id {id}."}

@router.delete("/{id}")
async def delete_todo(id: int):
    return {"msg": f"Delete todo at {id}."}
