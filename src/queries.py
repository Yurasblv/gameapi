from src.models import User, Game
from src.crud.abc import ModelType
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def search_user_db(db: AsyncSession, model: ModelType) -> ModelType:
    """Method return user model if it exists in db"""
    query = select(User).filter_by(name=model.dict()['name'])
    instances = await db.execute(query)
    if instances.scalars().first() is not None:
        raise Exception('This name for user exists')
    return model


async def search_game_db(db: AsyncSession, model: ModelType) -> ModelType:
    """Method return user model if it exists in db"""
    query = select(Game).filter_by(name=model.dict()['name'])
    instances = await db.execute(query)
    if instances.scalars().first() is not None:
        raise Exception('This name for game exists')
    return model
