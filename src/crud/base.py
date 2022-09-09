from src.crud.abc import AbstractCRUD, ModelType
from typing import Type, List
from sqlalchemy.orm import Session


class BaseCRUD(AbstractCRUD, ModelType):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: Session, *, data: ModelType) -> ModelType:
        db_obj = self.model(**data)
        db.add(db_obj)
        db.commit()
        return db_obj

    async def get_one(self, db: Session, *, id: int) -> ModelType:
        ...

    async def get_all(self, db: Session, *, page: int, per_page: int, **kwargs) -> List[ModelType]:
        ...

    async def update(self, db: Session, *, obj_in: ModelType, **kwargs) -> ModelType:
        ...

    async def delete(self, db: Session, *, id: int) -> ModelType:
        ...
