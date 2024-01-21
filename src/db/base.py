from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

engine = create_async_engine("sqlite+aiosqlite:///sqlite.db")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    id: Mapped[int] = mapped_column(primary_key=True)

async def get_acync_session():
    async with async_session_maker() as session:
        yield session