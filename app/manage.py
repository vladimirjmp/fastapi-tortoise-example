import asyncio
import sys

import typer
import uvicorn
from IPython import embed
from settings.db import init_tortoise

app = typer.Typer()


@app.command()
def runserver():
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)


@app.command()
def shell():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_tortoise())

    embed(colors='neutral', using='asyncio')

    loop.stop()
    sys.exit(0)


if __name__ == '__main__':
    app()
