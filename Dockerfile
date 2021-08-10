FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements/common.txt ./requirements.txt

RUN  pip install -r ./requirements.txt

COPY ./app /app

CMD [ "sh", "/start-reload.sh" ]