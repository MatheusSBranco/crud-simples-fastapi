from typing import Optional, Annotated

from sqlmodel import Field, SQLModel

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: Annotated[str, Field(min_length=3, max_length=50)]
    genre: Annotated[str, Field(min_length=3, max_length=20)]
    release_age: Annotated[int, Field(gt=0)]