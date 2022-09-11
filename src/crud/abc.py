from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Declarative class for DB model"""

    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


ModelType = TypeVar('ModelType', bound=Base)
SchemaType = TypeVar('SchemaType', bound=BaseModel)


class AbstractCRUD(ABC, Generic[ModelType, SchemaType]):

    @abstractmethod
    async def create(self, db: AsyncSession, *, data: SchemaType) -> ModelType:
        ...

    @abstractmethod
    async def get_one(self, db: AsyncSession, *, id: int) -> ModelType:
        ...

    @abstractmethod
    async def get_all(self, db: AsyncSession, *, page: int, per_page: int, **kwargs) -> List[ModelType]:
        ...

    @abstractmethod
    async def update(self, db: AsyncSession, *, obj_in: SchemaType, **kwargs) -> ModelType:
        ...

    @abstractmethod
    async def delete(self, db: AsyncSession, *, id: int) -> ModelType:
        ...
