from typing import Optional
from sqlmodel import SQLModel, Field

class TodoInput(SQLModel):
    title: str
    description: Optional[str] = Field(default=None)
    completed: Optional[bool] = Field(default=False)

class TodoOutput(TodoInput):
    id: Optional[int] = Field(default=None, primary_key=True)

class Todo(TodoOutput, table=True):
    pass
