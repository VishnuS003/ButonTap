# ButonTap

This project requires a Telegram bot token and a database connection string. 
Provide these values through environment variables or a `.env` file in the project root.

## Required environment variables

- `BOT_TOKEN` – token issued by BotFather for your Telegram bot.
- `DATABASE_URL` – database connection string. Example:
  `postgresql+asyncpg://user:password@host:5432/dbname`

Create a `.env` file with the following format:

```env
BOT_TOKEN=your_token_here
DATABASE_URL=postgresql+asyncpg://user:password@host:5432/dbname
```

The application will load these values automatically when starting.
