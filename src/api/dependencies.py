from repositories.tasks import TaskRepository
from repositories.users import UsersRepository
from services.tasks import TasksServices
from services.users import UsersService


def tasks_service():
    return TasksServices(TaskRepository)

def users_service():
    return UsersService(UsersRepository)