from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from dotenv import load_dotenv
import os
load_dotenv()

DB_URL = os.getenv('mysql_url')

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),index=True)
    biography = Column(String(50))
    books = relationship('Book', back_populates='owner')
    
class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(20),index=True)
    genre = Column(String(20))
    author_id = Column(Integer, ForeignKey(Author.id))
    owner = relationship('Author', back_populates='books')
        