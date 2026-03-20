import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import DB_URL
from app.models import Base

#Create connection to database
engine = create_engine(DB_URL, future=True)

#Starts a SQLAlchemy session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db() -> Generator[Session, None, None]:

    #Create a new database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    #Initializes table
    Base.metadata.create_all(bind=engine)