from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.operation import Base
from app.models.operation import Operation, OperationType
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///./math_operations.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
