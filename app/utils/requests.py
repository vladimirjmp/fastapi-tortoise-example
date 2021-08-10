import httpx
import requests

TIME_API_HOST = 'http://worldtimeapi.org/api/timezone'


async def get_current_time(timezone: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{TIME_API_HOST}/{timezone}')
        response.raise_for_status()

        response_data = response.json()
        current_time = response_data.get('datetime')

    return current_time


def get_current_time_sync(timezone: str) -> str:
    response = requests.get(f'{TIME_API_HOST}/{timezone}')
    response.raise_for_status()

    response_data = response.json()
    current_time = response_data.get('datetime')

    return current_time
