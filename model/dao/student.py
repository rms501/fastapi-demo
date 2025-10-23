from typing import Optional

from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    __tablename__ = "students"
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field()
    last_name: str = Field()
    age: int = Field()
    score: int = Field()