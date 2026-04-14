from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import BookCreate,BookResponse, AuthorCreate, AuthorResponse
from dbconfig import engine, SessionLocal, Base, Author, Book

app = FastAPI(title='Library management System')

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
            
@app.post('/author',response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

#create book for author
@app.post('/author/{author_id}/book')
def create_book_for_author(author_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail='Author not found')
    db_book = Book(**book.model_dump(), author_id = author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/authors/", response_model=List[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()