from dbConfig import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    
    posts = relationship('Posts',back_populates='owner')
    
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    content = Column(String(50))
    user_id = Column(Integer,ForeignKey('users.id'))
    
    owner = relationship('Users',back_populates='posts')
    