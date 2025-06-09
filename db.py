from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔧 ЗАМЕНИ на свои реальные данные PostgreSQL:
# Формат: postgresql+asyncpg://username:password@host:port/dbname
DATABASE_URL = "postgresql://gen_user:%5CX(2o%24Txzr%7C2V2@37.77.104.214:5432/default_db"

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
