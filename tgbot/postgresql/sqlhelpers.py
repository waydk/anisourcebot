from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from tgbot.postgresql.db import async_session
from tgbot.postgresql.models import Users


async def add_user(user: Users):
    try:
        async with async_session() as session:
            async with session.begin():
                session.add(user)
    except IntegrityError:
        pass
