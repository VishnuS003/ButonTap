from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db import async_session, Player

app = FastAPI()

# 👇 Разрешим Unity WebGL доступ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Лучше ограничить доменами
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/leaderboard")
async def get_leaderboard():
    async with async_session() as session:
        result = await session.execute(
            select(Player.username, Player.weekly_taps)
            .order_by(Player.weekly_taps.desc())
            .limit(10)
        )
        players = result.all()
        return {
            "players": [
                {"username": row.username, "weeklyTaps": row.weekly_taps}
                for row in players
            ]
        }
