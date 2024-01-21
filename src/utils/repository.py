from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    

class SQLAlchemyRepository(ABC):
    async def add_one():
        model = None
    
    async def find_all():
        