from pydantic import BaseModel, validator


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


class GameConnectSchema(GameSchema):
    user_id: int

    class Config:
        orm_mode = True
