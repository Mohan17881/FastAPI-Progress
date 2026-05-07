from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DBurl = 'sqlite:///./blog.db'

engine = create_engine(DBurl,
                       connect_args={'check_same_thread':False}
                       )

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()