import asyncio
from create_bot import dp, bot

async def main():
    # 💥 КЛЮЧЕВАЯ СТРОКА — убирает конфликт
    await bot.delete_webhook(drop_pending_updates=True)

    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
