from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from environs import Env

env = Env()
env.read_env()

PG_HOST = env("PG_HOST")
PG_USER = env("PG_USER")
PG_PASSWORD = env("PG_PASSWORD")
DATABASE = env("DATABASE")

POSTGRES_URI = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{DATABASE}"
engine = create_async_engine(POSTGRES_URI, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
