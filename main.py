from src.db import init_models, get_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas import UserSchema, GameSchema, GameConnectSchema
from fastapi import FastAPI
from fastapi import Depends
from fastapi.openapi.utils import get_openapi
from src.crud.user import user_repo
from src.crud.game import game_repo

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_models()


@app.post("/user/", response_model=UserSchema, description='Create user')
async def user_route(user: UserSchema, db: AsyncSession = Depends(get_session)):
    result = await user_repo.create(db=db, data=user)
    return result


@app.post("/game/", response_model=GameSchema, description='Create game')
async def game_route(game: GameSchema, db: AsyncSession = Depends(get_session)):
    result = await game_repo.create(db=db, data=game)
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
