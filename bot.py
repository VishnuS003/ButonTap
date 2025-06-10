import asyncio
import json
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from sqlalchemy.future import select
from db import async_session, Player

from fastapi import FastAPI

# Создаём FastAPI-приложение
api = FastAPI()

# Telegram Bot config
TOKEN = "7977201566:AAHan0eTiZV4ysjmGhM4uevvLcTw4qOuqfk"  # ← Замени на свой токен

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()

@router.message(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Play 🚀", web_app=WebAppInfo(url="https://butontapgame.vercel.app"))],
        [InlineKeyboardButton(text="Official channel", url="https://t.me/ButonTapGame")]
    ])
    await message.answer(
        "<b>🌷 Welcome to BUTON TAP!</b>\n\n"
        "💎 Tap the tulip, earn coins & diamonds!\n"
        "✨ Unlock boosters & grow your power.\n"
        "🎁 Get daily rewards.\n"
        "👥 Invite friends & get bonuses!",
        reply_markup=keyboard
    )

@router.message(lambda m: m.web_app_data is not None)
async def handle_webapp_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
    except json.JSONDecodeError:
        await message.answer("❌ Ошибка при разборе данных.")
        return

    async with async_session() as session:
        result = await session.execute(select(Player).where(Player.id == data["id"]))
        player = result.scalars().first()

        if not player:
            player = Player(
                id=data["id"],
                username=data.get("username", ""),
                telegram_user_id=message.from_user.id,
                taps=data.get("taps", 0),
                diamonds=data.get("diamonds", 0),
            )
            session.add(player)
        else:
            player.taps = data.get("taps", 0)
            player.diamonds = data.get("diamonds", 0)
            player.username = data.get("username", player.username)

        await session.commit()

    await message.answer("✅ Прогресс сохранён!")

dp.include_router(router)

@api.on_event("startup")
async def on_startup():
    asyncio.create_task(dp.start_polling(bot))

@api.get("/")
async def index():
    return {"status": "Bot is running on Timeweb Cloud 🚀"}