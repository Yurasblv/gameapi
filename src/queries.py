from src.models import User, Game, connection_table
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas import UserSchema, GameSchema, ConnectSchema
from fastapi.exceptions import HTTPException
from src.crud.abc import ModelType
from typing import Union


async def search_user_db(db: AsyncSession, schema: UserSchema) -> UserSchema:
    """Method return user model if it exists in db"""
    query = select(User).filter_by(name=schema.name)
    instances = await db.execute(query)
    if instances.scalars().first() is not None:
        raise HTTPException(status_code=409, detail="This name for user exists")
    return schema


async def search_game_db(db: AsyncSession, schema: GameSchema) -> GameSchema:
    """Method return user model if it exists in db"""
    query = select(Game).filter_by(name=schema.name)
    instances = await db.execute(query)
    if instances.scalars().first() is not None:
        raise HTTPException(status_code=409, detail="This name for game exists")
    return schema


async def create_instance_session_game(
    db: AsyncSession, schema: ConnectSchema
) -> Union[ValueError, ConnectSchema]:
    user_instance = await db.execute(select(User).where(User.name == schema.user))
    user = user_instance.scalars().first()
    game_instance = await db.execute(select(Game).where(Game.name == schema.name))
    game = game_instance.scalars().first()
    try:
        user, game = await check_connection(db, user, game)
    except TypeError:
        raise HTTPException(
            status_code=409, detail=f"User {user.name} already in {game.name}"
        )
    except AttributeError:
        raise HTTPException(status_code=409, detail=f"User or game was not found")
    user.game.append(game)
    await db.commit()
    return schema


async def check_connection(db: AsyncSession, user: ModelType, game: ModelType):
    instance = await db.execute(
        select(User)
        .join(connection_table)
        .join(Game)
        .where(Game.id == game.id)
        .where(User.id == user.id)
    )
    if instance.scalars().first() is None:
        return user, game
