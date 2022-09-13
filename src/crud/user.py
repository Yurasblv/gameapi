from typing import Type, Generic
from sqlalchemy import select, join
from src.crud.abc import AbcCRUD
from src.schemas import UserSchema, UserGamesSchema
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User
from src.queries import search_user_db
from src.crud.abc import ModelType, SchemaType, List
from sqlalchemy.orm import joinedload


class UserCRUD(AbcCRUD, Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AsyncSession, *, data: UserSchema) -> UserSchema:
        clean_data = await search_user_db(db=db, schema=data)
        db_obj = self.model(**clean_data.dict())
        db.add(db_obj)
        await db.commit()
        return data.from_orm(db_obj)

    async def get_all(self, db: AsyncSession, *, name: str) -> UserGamesSchema:
        instance = await db.execute(select(User).filter(User.name == name))
        model = instance.scalar()
        return UserGamesSchema.from_orm(model)


user_repo = UserCRUD(User)
