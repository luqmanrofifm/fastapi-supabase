from pydantic import BaseModel


class CreateBookRequest(BaseModel):
    title: str
    author: str
    year: int