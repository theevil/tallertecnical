import os
from typing import Generator
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from ..enitites import project, task 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set")

engine = create_engine(
    DATABASE_URL,
    echo=True,  
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(f"Error creating database tables: {e}")
        raise
