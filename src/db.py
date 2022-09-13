import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_async_engine(
    os.getenv("SQLALCHEMY_DATABASE_URI"),
    future=True,
    echo=True,
    pool_use_lifo=True,
    pool_pre_ping=True,
    pool_recycle=7200,
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def init_models():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        print("No connection to db. Details %s" % e)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
