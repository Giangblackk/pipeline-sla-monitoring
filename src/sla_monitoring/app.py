from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import Session, SQLModel, create_engine

from . import models

engine = create_engine("sqlite:///./database.db", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


class TaskEventCreate(BaseModel):
    task_name: str
    status: str
    event_time: datetime


@app.post("/job/status")
def post_job_status(task_event: TaskEventCreate):
    print(task_event.model_dump_json())
    print(task_event.event_time, type(task_event.event_time))
    task_event_rec = models.TaskEvent.model_validate(task_event)
    with Session(engine) as session:
        session.add(task_event_rec)
        session.commit()
        session.refresh(task_event_rec)
