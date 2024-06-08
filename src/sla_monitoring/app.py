from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import Session, SQLModel, create_engine

from . import models, scheduler_service

# %% database engine and start up function for database
engine = create_engine("sqlite:///./database.db", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# %% scheduler for background jobs
scheduler = scheduler_service.SchedulerService()


# %% FastAPI lifespan and app object
@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    create_db_and_tables()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


# %% Pydantic models for parsing requests
class TaskEventCreate(BaseModel):
    task_name: str
    status: str
    event_time: datetime


# %% API endpoints
@app.post("/job/status")
def post_job_status(task_event: TaskEventCreate):
    print(task_event.model_dump_json())
    print(task_event.event_time, type(task_event.event_time))
    task_event_rec = models.TaskEvent.model_validate(task_event)
    with Session(engine) as session:
        session.add(task_event_rec)
        session.commit()
        session.refresh(task_event_rec)
