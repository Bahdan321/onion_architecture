from typing import Annotated
from api.dependencies import tasks_service
from schemas.tasks import TaskSchemaAdd
from services.tasks import TasksServices

from fastapi import APIRouter, Depends


tasks_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    )

@tasks_router.post("")
async def add_tasks(
    task: TaskSchemaAdd,
    tasks_service: Annotated[TasksServices, Depends(tasks_service)],
):
    task_id = await tasks_service.add_task(task)


@tasks_router("")
async def get_tasks(
    tasks_service: Annotated[TasksServices, Depends(tasks_service)],
):
    tasks = await tasks_service.get_tasks()
    return tasks