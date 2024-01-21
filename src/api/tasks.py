from 

from fastapi import APIRouter, Depends


tasks_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    )

@tasks_router.post("")
async def add_tasks(
    task: Ta
)