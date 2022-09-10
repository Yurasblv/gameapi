from src.crud.base import BaseCRUD
from src.crud.abc import AbstractCRUD
from src.crud.abc import ModelType
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Game
from src.queries import search_game_db


class GameCRUD(BaseCRUD, AbstractCRUD):

    async def create(self, db: AsyncSession, *, data: ModelType) -> ModelType:
        clean_data = await search_game_db(db=db, model=data)
        schema = await super().create(db=db, data=clean_data)
        return schema


game_repo = GameCRUD(Game)