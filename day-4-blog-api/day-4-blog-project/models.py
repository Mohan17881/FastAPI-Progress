from pydantic import BaseModel


class UserCreate(BaseModel):

    name: str

    email: str
    
class UserResponse(BaseModel):

    id: int

    name: str

    email: str

    class Config:
        orm_mode = True    
        
class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int        
    
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    
    class config:
        orm_mode = True    
        
class UserWithPosts(BaseModel):
    id: int

    name: str

    posts: list[PostResponse]

    class Config:
        orm_mode = True        