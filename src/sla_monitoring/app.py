from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Msg(BaseModel):
    task_name: str
    status: str


@app.post("/job/status")
def post_job_status(msg: Msg):
    print(msg.model_dump_json())
