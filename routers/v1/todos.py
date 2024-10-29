from fastapi import APIRouter, HTTPException
from models.todo import Todo, TodoInput, TodoOutput
from db import SessionDep
from sqlmodel import select

router = APIRouter(prefix="/todos")

@router.get("/", response_model=list[TodoOutput])
async def read_todos(session: SessionDep):
    todos = session.exec(select(Todo)).all()

    return todos

@router.post("/", response_model=TodoOutput)
async def create_todo(todo: TodoInput, session: SessionDep):
    todo = Todo.model_validate(todo)

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo

@router.get("/{id}", response_model=TodoOutput)
async def read_todo(id: int, session: SessionDep):
    todo = session.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    return todo

@router.put("/{id}")
async def update_todo(id: int, todo_patch: TodoInput, session: SessionDep):
    todo = session.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    todo_data = todo_patch.model_dump(exclude_unset=True)
    todo.sqlmodel_update(todo_data)

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo

@router.delete("/{id}", status_code=204)
async def delete_todo(id: int, session: SessionDep):
    todo = session.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    session.delete(todo)
    session.commit()
