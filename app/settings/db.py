from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from settings.constants import DB_URL

MODULES = {'models': ['apis.timezone.models']}


def register_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DB_URL,
        modules=MODULES,
        generate_schemas=True,
        add_exception_handlers=True
    )


async def init_tortoise() -> None:
    await Tortoise.init(
        db_url=DB_URL,
        modules=MODULES,
    )
    # await Tortoise.generate_schemas()
