from repositories.tasks import TaskRepository
from repositories.users import UsersRepository
from services.tasks import TasksService
from services.users import UsersService


def tasks_service():
    return TasksService(TaskRepository)

def users_service():
    return UsersService(UsersRepository)