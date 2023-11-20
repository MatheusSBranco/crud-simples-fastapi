from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    genre: str
    release_age: int