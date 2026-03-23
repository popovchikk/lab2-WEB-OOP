# database.py - подключение к PostgreSQL

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# создаю движок
engine = create_async_engine(DATABASE_URL, echo=True)

# сессия для работы с БД
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# базовый класс для моделей
Base = declarative_base()


# функция для создания таблиц
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# функция для получения сессии
async def get_session():
    async with async_session() as session:
        yield session