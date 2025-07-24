from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.workers.queue_worker import process_math_tasks
from app.db.database import SessionLocal, init_db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create FastAPI app
app = FastAPI(title="Math Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    import asyncio
    init_db()
    asyncio.create_task(process_math_tasks())

# Simple health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}