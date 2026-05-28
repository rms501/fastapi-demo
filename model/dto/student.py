from pydantic import BaseModel, ConfigDict


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    score: int

    model_config = ConfigDict(from_attributes=True)
