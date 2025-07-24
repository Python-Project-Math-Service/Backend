from pydantic import BaseModel, Field


class PowRequest(BaseModel):
    base: float
    exponent: float


class FactorialRequest(BaseModel):
    number: int = Field(..., ge=0)


class FibonacciRequest(BaseModel):
    index: int = Field(..., ge=0)
