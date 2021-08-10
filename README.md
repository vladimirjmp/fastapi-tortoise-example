# fastapi-tortoise-example

This is a fastAPI practice using tortoise-orm. The API exposes some endpoints to save cities and their timezones and then fetch the current timezone.

## Instructions

Update database env vars in `env.docker` file:

    DB_NAME=tortoise-test
    DB_USER=user
    DB_PASSWORD=passwd
    DB_PORT=5499

Then run the following command

`$ docker compose --env-file env.docker up -d`

Finally go to the browser and search for `http://localhost:8000/docs`