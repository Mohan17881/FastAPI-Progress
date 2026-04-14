from pydantic import BaseModel
from typing import List


class BookBase(BaseModel):
    name: str
    genre: str

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    author_id: int
    class Config:
        from_attributes = True


class AuthorBase(BaseModel):
    name: str
    biography: str

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    books: List[BookResponse] = []

    class Config:
        from_attributes = True