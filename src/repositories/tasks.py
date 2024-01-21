from utils.repository import SQLAlchemyRepository
from models.tasks import Tasks

class TaskRepository(SQLAlchemyRepository):
    model = Tasks