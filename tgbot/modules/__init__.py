from tgbot.modules.search import search_source
from tgbot.modules.start import start_command
from aiogram import Dispatcher, types

def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(search_source, content_types=types.ContentType.PHOTO)
