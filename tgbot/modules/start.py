from loguru import logger
from aiogram.types import Message


async def start_command(message: Message):
    """
    Responds to /start
    :param message:
    :return:
    """
    user = message.from_user.full_name
    logger.info(f"{user} send /start")
    await message.answer(
        f"Hi, <b>{user}</b>, this bot was created"
        "to find the original source of anime, manga and art."
    )
