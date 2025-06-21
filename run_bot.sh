#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
nohup python bot.py > bot.log 2>&1 &
echo "Бот запущен в фоне. Логи → bot.log"
