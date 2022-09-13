from src.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

connection_table = Table(
    "connection",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("game_id", ForeignKey("games.id")),
)


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    user = relationship(
        "User", secondary=connection_table, back_populates="game", lazy="joined"
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    game = relationship(
        "Game", secondary=connection_table, back_populates="user", lazy="joined"
    )
