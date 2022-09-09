from src.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    game = relationship("Game", cascade='all,delete', backref="user")


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
