import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message

# Инициализация бота
bot = Bot(token="7977201566:AAHan0eTiZV4ysjmGhM4uevvLcTw4qOuqfk", parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Привет! Бот запущен без БД 🌷")

async def main():
    print("✅ Запуск Telegram-бота...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

