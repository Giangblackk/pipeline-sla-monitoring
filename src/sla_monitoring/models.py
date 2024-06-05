from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class TaskEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_name: str
    status: str
    event_time: datetime
