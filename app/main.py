from fastapi import FastAPI
from app.api.routes import router
from app.workers.queue_worker import process_math_tasks
from fastapi import Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.db.database import init_db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="Math Microservice")
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    import asyncio
    init_db()
    asyncio.create_task(process_math_tasks())

@app.get("/health")
async def health_check():
    return {"status": "ok"}