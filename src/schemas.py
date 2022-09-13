from pydantic import BaseModel, validator
from typing import List, Optional


class UserSchema(BaseModel):
    name: str
    age: int
    email: str

    class Config:
        orm_mode = True

    @validator("name")
    def name_validator(cls, value: str):
        if len(value) < 4:
            raise ValueError("Username too short")
        if len(value) > 30:
            raise ValueError("Username too long")
        return value

    @validator("age")
    def age_validator(cls, value: int):
        if value < 0:
            raise ValueError("Age must be bigger")
        if value > 100:
            raise ValueError("Age must be lower")
        return value


class GameSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True

    @validator("name")
    def name_validator(cls, value: str):
        if len(value) < 4:
            raise ValueError("Username too short")
        if len(value) > 30:
            raise ValueError("Username too long")
        return value


class ConnectSchema(GameSchema):
    user: str

    class Config:
        orm_mode = True


class GameConnectsSchema(GameSchema):
    user: Optional[List[UserSchema]]

    class Config:
        orm_mode = True


class UserGamesSchema(UserSchema):
    game: Optional[List[GameSchema]]

    class Config:
        orm_mode = True
