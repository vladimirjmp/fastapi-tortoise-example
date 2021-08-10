from fastapi import FastAPI
from settings.constants import DB_URL
from tortoise.contrib.fastapi import register_tortoise


def register_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DB_URL,
        modules={'models': ['apis.timezone.models']},
        generate_schemas=True,
        add_exception_handlers=True
    )
