import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 🔧 ЗАМЕНИ на свои реальные данные PostgreSQL:
# Load environment variables from a .env file if present
load_dotenv()

# Database connection string should be provided via the DATABASE_URL
# environment variable. Example format:
# postgresql+asyncpg://username:password@host:port/dbname
DATABASE_URL = os.getenv("postgresql://gen_user:%5CX(2o%24Txzr%7C2V2@37.77.104.214:5432/default_db")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

# Создание движка и асинхронной сессии
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Модель игрока
class Player(Base):
    __tablename__ = "players"

    id = Column(String, primary_key=True)  # Telegram ID или уникальный ID из WebApp
    username = Column(String)
    taps = Column(Integer)
    diamonds = Column(Integer)
    telegram_user_id = Column(Integer)

# Функция для первичной инициализации таблицы
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
