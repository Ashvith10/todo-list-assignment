from fastapi import FastAPI
from routers.v1 import todos

app = FastAPI()
app.include_router(todos.router, prefix="/api/v1")
