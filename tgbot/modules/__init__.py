from tgbot.modules.start import start_command
from aiogram import Dispatcher

def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")