from fastapi import FastAPI

from routers import views
from settings.db import register_db
from utils.exception_handlers import register_exception_handlers

app = FastAPI(title="Tortoise ORM FastAPI example")

app.include_router(
    views.router,
    prefix='/api'
)


@app.get('/', include_in_schema=False)
def index():
    return {
        'message': 'Welcome home!!'
    }


register_db(app)
register_exception_handlers(app)
