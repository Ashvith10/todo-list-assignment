from fastapi import FastAPI
from db import init_db
from routers.v1 import todos

app = FastAPI(
    title="todo-list-application",
    summary="A take-home assignment for `Bugs and Glitches`.",
    redoc_url=None
)
app.include_router(todos.router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    init_db()
