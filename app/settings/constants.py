import os

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_URL = (
    f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
)
