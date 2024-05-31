from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Msg(BaseModel):
    job_name: str
    run_id: str
    run_config: dict
    status: str
    step_key: Optional[str]
    dagster_event: Optional[str]

@app.post("/job/status")
def post_job_status(msg: Msg):
    print(msg)
