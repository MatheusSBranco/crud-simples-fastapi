from typing import Optional, Annotated
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: Annotated[str, Field(min_length=5, max_length=20)]
    email: EmailStr
    hashed_password: str