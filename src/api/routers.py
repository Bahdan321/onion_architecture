from api.tasks import tasks_router
from api.users import users_router

all_routers = [
    tasks_router,
    users_router,
]