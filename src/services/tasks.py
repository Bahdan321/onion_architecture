from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    )