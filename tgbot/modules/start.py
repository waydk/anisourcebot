from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from loguru import logger
from aiogram.types import Message


async def start_command(message: Message):
    """Bot command /start

    Args:
        message (Message): To send a message to a user
    """
    keyboard = InlineKeyboardMarkup(row_width=3)

    keyboard.add(
        InlineKeyboardButton('github', url='https://github.com/waydk/anisourcebot')
    )

    user = message.from_user.full_name
    logger.info(f"{user} send /start")
    await message.answer(
        f"Hi, <b>{user}</b>, this bot was created"
        " to find the original source of anime, manga and art.\n\n"
        "<i>Just send a photo.</i>",
        reply_markup=keyboard
    )
