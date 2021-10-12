from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from loguru import logger
from aiogram.types import Message

from tgbot.postgresql.models import Users
from tgbot.postgresql.sqlhelpers import add_user


async def start_command(message: Message):
    """Bot command /start

    Args:
        message (Message): To send a message to a user
    """
    keyboard = InlineKeyboardMarkup(row_width=3)

    keyboard.add(
        InlineKeyboardButton('github', url='https://github.com/waydk/anisourcebot')
    )

    user = message.from_user

    # Add to database
    user_db = Users(user_id=message.from_user.id,
                    first_name=user.first_name,
                    last_name=user.last_name)
    await add_user(user_db)

    logger.info(f"{user} send /start")
    await message.answer(
        f"Hi, <b>{user.full_name}</b>, this bot was created"
        " to find the original source of anime, manga and art.\n\n"
        "<i>Just send a photo.</i>",
        reply_markup=keyboard
    )
