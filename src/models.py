from src.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

connection_table = Table(
    "connection",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("game_id", ForeignKey("game.id")),
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    game = relationship("Game", secondary=connection_table, backref="user"
                        )


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String)
