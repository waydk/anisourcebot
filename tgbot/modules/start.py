from aiogram.types import Message


async def start_command(message: Message):
    """
    Responds to /start
    :param message:
    :return:
    """
    await message.answer("Hello, world!")
