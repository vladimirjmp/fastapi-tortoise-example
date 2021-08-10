import asyncio
import sys

import typer
import uvicorn
from IPython import embed
from tortoise import Tortoise

app = typer.Typer()


@app.command()
def runserver():
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)


@app.command()
def shell():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())

    embed(colors='neutral')

    loop.stop()
    sys.exit(0)


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['apis.timezone.models']}
    )
    # await Tortoise.generate_schemas()

if __name__ == '__main__':
    app()
