from fastapi import FastAPI
from db import init_db
from routers.v1 import todos

app = FastAPI()
app.include_router(todos.router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    init_db()
