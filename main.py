import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Базовая настройка SQLAlchemy
DATABASE_URL = "psql 'postgresql://gen_user:%5CX(2o%24Txzr%7C2V2@37.77.104.214:5432/default_db'"  # ← ЗАМЕНИ на свои данные

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Инициализация бота
bot = Bot(token="7977201566:AAHan0eTiZV4ysjmGhM4uevvLcTw4qOuqfk", parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Привет! Бот подключён к базе данных 🌱")

async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ База данных подключена")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

