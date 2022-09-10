from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
ModelType = TypeVar('ModelType', bound=BaseModel)


class AbstractCRUD(ABC, Generic[ModelType]):

    @abstractmethod
    async def create(self, db: AsyncSession, *, data: ModelType) -> ModelType:
        ...

    @abstractmethod
    async def get_one(self, db: AsyncSession, *, id: int) -> ModelType:
        ...

    @abstractmethod
    async def get_all(self, db: AsyncSession, *, page: int, per_page: int, **kwargs) -> List[ModelType]:
        ...

    @abstractmethod
    async def update(self, db: AsyncSession, *, obj_in: ModelType, **kwargs) -> ModelType:
        ...

    @abstractmethod
    async def delete(self, db: AsyncSession, *, id: int) -> ModelType:
        ...
