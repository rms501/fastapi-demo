from pydantic import BaseModel


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    score: int

    class Config:
        orm_mode = True