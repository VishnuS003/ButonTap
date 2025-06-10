from sqlalchemy import Column, Integer, String
from db import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(String, primary_key=True)
    telegram_user_id = Column(Integer)
    username = Column(String)
    taps = Column(Integer, default=0)
    diamonds = Column(Integer, default=0)
    weekly_taps = Column(Integer, default=0)  # 👈 ОБЯЗАТЕЛЕН

