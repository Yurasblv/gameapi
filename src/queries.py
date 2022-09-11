from src.models import User, Game
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas import UserSchema, GameSchema
from fastapi.exceptions import HTTPException


async def search_user_db(db: AsyncSession, model: UserSchema) -> UserSchema:
    """Method return user model if it exists in db"""
    query = select(User).filter_by(name=model.dict()['name'])
    instances = await db.execute(query)
    if instances.scalars().first() is not None:
        raise HTTPException(status_code=409, detail='This name for user exists')
    return model


async def search_game_db(db: AsyncSession, model: GameSchema) -> GameSchema:
    """Method return user model if it exists in db"""
    query = select(Game).filter_by(name=model.dict()['name'])
    instances = await db.execute(query)
    if instances.scalars().first() is not None:
        raise HTTPException(status_code=409, detail='This name for game exists')
    return model
