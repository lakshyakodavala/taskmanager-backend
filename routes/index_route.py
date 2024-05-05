from fastapi import APIRouter
from config.db_config import connect_database
from schema.user_schema import UserLoginRequest, UserRegisterRequest
from schema.task_schema import TaskCreateRequest
from services.user_service import UserService
from services.task_service import TaskService
from fastapi.responses import JSONResponse
from fastapi import Query

router = APIRouter()
conn = connect_database()

user_service = UserService()
task_service = TaskService()


@router.post("/register")
def register_user(request: UserRegisterRequest):
    response = user_service.register_user(conn, request.email, request.password)
    return JSONResponse(
        status_code=response['status_code'],
        content={"message": response['message'], "data": response['data']}
    )


@router.post("/login")
def login_user(request: UserLoginRequest):
    response = user_service.login_user(conn, request.email, request.password)
    return JSONResponse(
        status_code=response['status_code'],
        content={"message": response['message'], "data": response['data']}
    )


@router.post("/task-create")
def create_task(request: TaskCreateRequest):
    response = task_service.create_task(conn, request.task_name, request.task_description,
                                        request.task_status, request.task_tag, request.created_by)
    return JSONResponse(
        status_code=response['status_code'],
        content={"message": response['message']}
    )


@router.put("/task-update/{task_id}")
def update_task(task_id: int, request: TaskCreateRequest):
    response = task_service.update_task(conn, task_id, request.task_name, request.task_description,
                                        request.task_status, request.task_tag)
    return JSONResponse(
        status_code=response['status_code'],
        content={"message": response['message']}
    )


@router.delete("/task-delete/{task_id}")
def delete_task(task_id: int):
    response = task_service.delete_task(conn, task_id)
    return JSONResponse(
        status_code=response['status_code'],
        content={"message": response['message']}
    )


@router.get("/tasks")
def get_all_tasks(page: int = Query(default=1), limit: int = Query(default=10), status: str = Query(default=None)):
    response = task_service.fetch_all_tasks(conn, page, limit, status)
    return JSONResponse(
        status_code=response['status_code'],
        content={"message": response['message'], "data": response['data'], "count": response['count']}
    )
