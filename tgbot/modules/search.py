from environs import Env
from aiogram.types import Message
from PicImageSearch import AsyncSauceNAO, NetWork

async def search_source(message: Message):
    env = Env()
    env.read_env()
    api_key = env.str("SAUCE_API")
    async with NetWork() as client:
        saucenao = AsyncSauceNAO(client=client, api_key=api_key)
        res = await saucenao.search('https://pixiv.cat/77702503-1.jpg')
        await message.answer(res.raw[0].title)
