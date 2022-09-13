from src.db import init_models, get_session
from src.crud.user import user_repo
from src.crud.game import game_repo
from src.schemas import (
    UserSchema,
    GameSchema,
    ConnectSchema,
    UserGamesSchema,
    GameConnectsSchema,
)
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI
from fastapi import Depends
from fastapi.openapi.utils import get_openapi

tags_metadata = [
    {
        "name": "User Instance",
        "description": "Create user profile",
    },
    {
        "name": "Game Instance",
        "description": "Create new game",
    },
    {
        "name": "Play the game",
        "description": "Connect to chosen game wia user name and game title name",
    },
    {
        "name": "User Profile",
        "description": "Describe user info and game sessions",
    },
    {
        "name": "Game Player",
        "description": "Describe which players in game",
    },
]

app = FastAPI(docs_url="/", openapi_tags=tags_metadata, redoc_url=None)


@app.on_event("startup")
async def startup_event():
    await init_models()


@app.post(
    "/user/",
    response_model=UserSchema,
    description="Create user",
    tags=["User Instance"],
)
async def user_route(user: UserSchema, db: AsyncSession = Depends(get_session)):
    result = await user_repo.create(db=db, data=user)
    return result


@app.post(
    "/game/",
    response_model=GameSchema,
    description="Create game",
    tags=["Game Instance"],
)
async def game_route(game: GameSchema, db: AsyncSession = Depends(get_session)):
    result = await game_repo.create(db=db, schema=game)
    return result


@app.post("/connect/", description="Create game session", tags=["Play the game"])
async def connect_route(game: ConnectSchema, db: AsyncSession = Depends(get_session)):
    result = await game_repo.connection(db=db, schema=game)
    return result


@app.get(
    "/user",
    response_model=UserGamesSchema,
    description="User information",
    tags=["User Profile"],
)
async def user_info(name: str, db: AsyncSession = Depends(get_session)):
    result = await user_repo.get_all(db=db, name=name)
    return result


@app.get(
    "/game",
    response_model=GameConnectsSchema,
    description="Game information",
    tags=["Game Player"],
)
async def game_connects(name: str, db: AsyncSession = Depends(get_session)):
    result = await game_repo.get_all(db=db, name=name)
    return result


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="GAMEPLAY",
        version="2.5.0",
        description="Schema for Game Api service",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
