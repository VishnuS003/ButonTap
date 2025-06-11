from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="7977201566:AAHan0eTiZV4ysjmGhM4uevvLcTw4qOuqfk", parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Привет! Бот работает 🌷")

if __name__ == "__main__":
    executor.start_polling(dp)