from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    task_name: str
    task_description: str
    task_status: str
    task_tag: str
    created_by: str
