import asyncio
from aiogram import Bot, Dispatcher, types

bot = Bot(token="7977201566:AAHan0eTiZV4ysjmGhM4uevvLcTw4qOuqfk", parse_mode="HTML")
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Бот работает 🌷")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(lambda _: print("✅ Бот запущен"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
