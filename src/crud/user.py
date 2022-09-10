from src.crud.base import BaseCRUD
from src.crud.abc import AbstractCRUD
from src.crud.abc import ModelType
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User
from src.queries import search_user_db


class UserCRUD(BaseCRUD, AbstractCRUD):

    async def create(self, db: AsyncSession, *, data: ModelType) -> ModelType:
        clean_data = await search_user_db(db=db, model=data)
        schema = await super().create(db=db, data=clean_data)
        return schema


user_repo = UserCRUD(User)
