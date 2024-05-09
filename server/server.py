import asyncio
from aiogram import Bot, Dispatcher, F
from  aiogram.types import Message
from dotenv import load_dotenv
import os
from hadnlers import router

bot = None
dp = Dispatcher()


async def main():
    load_dotenv()
    bot = Bot(os.getenv("TOKEN"))
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())