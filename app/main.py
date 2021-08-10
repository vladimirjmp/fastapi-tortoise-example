from fastapi import FastAPI
from routers import views
from settings.db import register_db

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
