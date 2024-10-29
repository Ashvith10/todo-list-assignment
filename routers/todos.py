from fastapi import APIRouter

router = APIRouter(prefix="/todos")

@router.get("/")
async def get_root():
    return {"msg": "Get all todos"}
