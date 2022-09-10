from src.crud.abc import AbstractCRUD, ModelType
from typing import Type, List, Generic
from sqlalchemy.ext.asyncio import AsyncSession


class BaseCRUD(AbstractCRUD, Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AsyncSession, *, data: ModelType) -> ModelType:
        db_obj = self.model(**data.dict())
        db.add(db_obj)
        await db.commit()
        return data.from_orm(db_obj)

    async def get_one(self, db: AsyncSession, *, id: int) -> ModelType:
        ...

    async def get_all(self, db: AsyncSession, *, page: int, per_page: int, **kwargs) -> List[ModelType]:
        ...

    async def update(self, db: AsyncSession, *, obj_in: ModelType, **kwargs) -> ModelType:
        ...

    async def delete(self, db: AsyncSession, *, id: int) -> ModelType:
        ...
