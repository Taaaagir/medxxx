import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = "8063265091:AAESmXvjW1z3esWyILITzJTxqemKnAdT9nk"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
    # 💥 УБИРАЕТ КОНФЛИКТ (ОЧЕНЬ ВАЖНО)
    await bot.delete_webhook(drop_pending_updates=True)

    # 🚀 запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
