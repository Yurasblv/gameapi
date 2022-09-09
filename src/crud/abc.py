from abc import ABC, abstractmethod
from typing import TypeVar, Dict, List
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar('ModelType', bound=BaseModel)


class AbstractCRUD(ABC, ModelType):

    @abstractmethod
    async def create(self, db: Session, *, data: ModelType) -> ModelType:
        ...

    @abstractmethod
    async def get_one(self, db: Session, *, id: int) -> ModelType:
        ...

    @abstractmethod
    async def get_all(self, db: Session, *, page: int, per_page: int, **kwargs) -> List[ModelType]:
        ...

    @abstractmethod
    async def update(self, db: Session, *, obj_in: ModelType, **kwargs) -> ModelType:
        ...

    @abstractmethod
    async def delete(self, db: Session, *, id: int) -> ModelType:
        ...
