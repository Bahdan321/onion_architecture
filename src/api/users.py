from typing import Annotated
from api.dependencies import users_service
from schemas.users import UserSchemaAdd
from services.users import UsersService

from fastapi import APIRouter, Depends

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@users_router.post("")
async def add_user(
    user: UserSchemaAdd,
    users_service: Annotated[UsersService, Depends(users_service)],
):
    user_id = await users_service.add_user(user)
    return {
        "user_id": user_id,
    }

@users_router.get("")
async def get_users(
    users_service: Annotated[UsersService, Depends(users_service)],
):
    users = await users_service.get_users()
    return users