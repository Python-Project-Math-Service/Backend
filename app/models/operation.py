from sqlalchemy import Column, Integer, Float, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class OperationType(str, enum.Enum):
    pow = "pow"
    factorial = "factorial"
    fibonacci = "fibonacci"


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(Enum(OperationType), nullable=False)
    operand1 = Column(Float, nullable=False)
    operand2 = Column(Float, nullable=True)
    result = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
