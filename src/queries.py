from src.db import *
from typing import Union
from src.crud.abc import ModelType
from sqlalchemy.orm import Session


def search_user_db(model: ModelType) -> Union[ModelType, Exception]:
    """Method return user model if it exists in db"""
    if Session.query(User.query.all()).filter_by(username=model.username).count() >= 1:
        raise ValueError("User Exists")
    else:
        return model
