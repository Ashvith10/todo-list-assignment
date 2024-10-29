from typing import Optional
from pydantic import BaseModel, Field

class TodoIn(BaseModel):
    title: str
    description: Optional[str] = Field(default=None)
    completed: Optional[bool] = Field(default=False)

class TodoOut(TodoIn):
    id: Optional[int] = Field(default=None, primary_key=True)
