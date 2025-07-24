from fastapi import APIRouter
from app.models.request_models import PowRequest, FactorialRequest, FibonacciRequest
from app.services import calculator
from app.workers.queue_worker import math_task_queue
import asyncio
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.models.operation import OperationType, Operation

router = APIRouter()


@router.post("/pow")
async def calculate_power(request: PowRequest, db: Session = Depends(get_db)):
    result = calculator.calculate_pow(request.base, request.exponent)
    new_op = Operation(
        operation=OperationType.pow,
        operand1=request.base,
        operand2=request.exponent,
        result=result
    )
    db.add(new_op)
    db.commit()
    return {"result": result}


@router.post("/factorial")
async def calculate_factorial(request: FactorialRequest, db: Session = Depends(get_db)):
    future = asyncio.get_event_loop().create_future()
    await math_task_queue.put(("factorial", request.dict(), future))
    result = await future
    new_op = Operation(
        operation=OperationType.factorial,
        operand1=request.number,
        operand2=None,
        result=result
    )
    db.add(new_op)
    db.commit()
    return {"result": result}


@router.post("/fibonacci")
async def calculate_fibonacci(request: FibonacciRequest, db: Session = Depends(get_db)):
    future = asyncio.get_event_loop().create_future()
    await math_task_queue.put(("fibonacci", request.dict(), future))
    result = await future
    new_op = Operation(
        operation=OperationType.fibonacci,
        operand1=request.index,
        operand2=None,
        result=result
    )
    db.add(new_op)
    db.commit()
    return {"result": result}
