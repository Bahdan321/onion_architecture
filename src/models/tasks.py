from db.base import Base
from schemas.tasks import TaskSchema

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Tasks(Base):

    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            title=self.title,
            author_id=self.author_id,
            assignee_id=self.assignee_id,
        )