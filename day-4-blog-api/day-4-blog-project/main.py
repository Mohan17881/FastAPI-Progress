from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from sqlalchemy import select

from typing import Annotated

from dbConfig import engine, SessionLocal
from schemas import Base, Users, Posts
from models import PostCreate,PostResponse,UserCreate,UserResponse,UserWithPosts

app = FastAPI(title='Blog Page')

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
            
db_dependency = Annotated[Session,Depends(get_db)]

@app.post('/users',response_model=UserResponse)
def create_user(user: UserCreate, db: db_dependency):
    user_data = Users(**user.model_dump())
    
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    
    return user_data

@app.post('/posts')
def create_post(post:PostCreate,db:db_dependency):
    post_data = Posts(**post.model_dump())
    
    db.add(post_data)
    db.commit()
    db.refresh(post_data)
    
    return post_data

@app.get('/posts')
def all_posts(db:db_dependency):
    
    all_posts = db.query(Posts).order_by(Posts.id.desc()).all()
    
    return all_posts

@app.get('/Posts/{user_id}',response_model=UserWithPosts)
def posts_with_user_id(user_id: int,db:db_dependency):
    user = db.query(Users).filter(Users.id == user_id).first()
    
    return user
