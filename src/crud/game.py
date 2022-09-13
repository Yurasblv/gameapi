from src.crud.abc import AbcCRUD
from src.crud.abc import ModelType
from sqlalchemy.ext.asyncio import AsyncSession
from src.queries import search_game_db, create_instance_session_game
from src.models import Game
from src.schemas import GameSchema, ConnectSchema, GameConnectsSchema
from typing import Union, Generic, Type
from fastapi.exceptions import HTTPException
from src.crud.abc import SchemaType
from sqlalchemy import select


class GameCRUD(AbcCRUD, Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_all(self, db: AsyncSession, *, name) -> GameConnectsSchema:
        instance = await db.execute(select(Game).filter(Game.name == name))
        model = instance.scalars().first()
        return GameConnectsSchema.from_orm(model)

    async def create(self, db: AsyncSession, *, schema: ModelType) -> GameSchema:
        clean_data = await search_game_db(db=db, schema=schema)
        db_obj = self.model(**clean_data.dict())
        db.add(db_obj)
        await db.commit()
        return schema.from_orm(db_obj)

    async def connection(
        self, db: AsyncSession, *, schema: ConnectSchema
    ) -> Union[HTTPException, ConnectSchema]:
        result = await create_instance_session_game(db=db, schema=schema)
        return result


game_repo = GameCRUD(Game)
