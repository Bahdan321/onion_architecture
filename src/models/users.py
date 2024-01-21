from db.base import Base
from schemas.users import UserSchema

from sqlalchemy.orm import Mapped, mapped_column

class Users(Base):

    name: Mapped[str]

    def to_read_moedl(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
        )