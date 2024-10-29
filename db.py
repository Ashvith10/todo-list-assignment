from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session

file_name = "db.sqlite3"
engine = create_engine(f"sqlite:///{file_name}", echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
