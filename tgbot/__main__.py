import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from tgbot import modules
from environs import Env
from tgbot.postgresql.db import engine
from tgbot.postgresql.models import Base


async def main():
    env = Env()
    env.read_env()
    token = env.str("BOT_TOKEN")

    logger.info("Start database...")
    async with engine.begin() as conn:
        # Create tables
        await conn.run_sync(Base.metadata.create_all)

    bot = Bot(token=token, parse_mode='html')
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    logger.info("Configuring modules...")
    modules.setup(dp)

    logger.info("Start polling")
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
