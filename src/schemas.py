from pydantic import BaseModel, validator
from typing import AnyStr


class User(BaseModel):
    name: AnyStr
    age: int
    email: AnyStr

    @validator("name")
    def name_validator(cls, value: AnyStr):
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


class Game(BaseModel):
    name: AnyStr
    user_id: int

    @validator("name")
    def name_validator(cls, value: AnyStr):
        if len(value) < 4:
            raise ValueError("Username too short")
        if len(value) > 30:
            raise ValueError("Username too long")
        return value