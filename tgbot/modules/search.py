import os

from aiogram import Bot
from environs import Env
from aiogram.types import Message
from PicImageSearch import AsyncSauceNAO, NetWork
from loguru import logger

async def saucenao_search(message: Message, api_key: str, photo_path: str):
    """Api saucenao search

    Args:
        message (aiogram.types.Message): sending a message to a user
        api_key (str): to access the api
        photo_path (str): the path to the photo that is searched for
    """
    async with NetWork() as client:
        saucenao = AsyncSauceNAO(client=client, api_key=api_key)
        res = await saucenao.search(photo_path)

        try:
            est_time = f"☁ Est Time: {res.origin['results'][0]['data']['est_time']}\n"
        except KeyError:
            est_time = ''

        try:
            part = f"☁ Part: {res.origin['results'][0]['data']['part']}\n"
        except KeyError:
            part = ''

        res = res.raw[0]
        author = f"☁ Author: {res.author}\n" if res.author else ''

    await message.answer(f"☁ Title: {res.title}\n"
                         f"☁ Similarity: {res.similarity}%\n"
                         f"{author}"
                         f"{est_time}"
                         f"{part}"
                         f"☁ Url: {res.url}")


async def search_source(message: Message):
    """The function gets the message,
     takes the photo id from it and downloads
     the photo, then searches for the original source

    Args:
        message (Message): aiogram.types.Message
    """
    # Get token and sauce api from env
    env = Env()
    env.read_env()

    token = env.str("BOT_TOKEN")
    api_key = env.str("SAUCE_API")

    photo_path = os.path.join('tgbot', 'photos', 'search_photo.jpg')

    #  Download photo
    bot = Bot(token=token, parse_mode='html')
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    await bot.download_file(file_path, photo_path)

    try:
        await saucenao_search(message, api_key, photo_path)
    except Exception as err:
        logger.debug(err)
