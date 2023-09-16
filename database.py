from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings as s

DATABASE_URL = f"postgresql+asyncpg://{s.DB_USER}:{s.DB_PASSWORD}@{s.DB_HOST}:{s.DB_PORT}/{s.DB_NAME}"

engine = create_async_engine(DATABASE_URL)
session = async_sessionmaker(class_=AsyncSession(), bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
