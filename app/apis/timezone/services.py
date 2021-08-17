import logging
from typing import Any, Dict
from uuid import UUID

from tortoise.exceptions import DoesNotExist

from apis.timezone.models import City, City_Pydantic, CityIn_Pydantic

logger = logging.getLogger(__name__)


async def get_cities():
    return await City_Pydantic.from_queryset(City.all())


async def get_city(*, city_id: UUID) -> Dict[str, Any]:
    city = await get_city_by_id(city_id=city_id)
    return await City_Pydantic.from_tortoise_orm(city)


async def create_city(*, city: CityIn_Pydantic) -> Dict[str, Any]:
    new_city = await City.create(**city.dict(exclude_unset=True))
    return await CityIn_Pydantic.from_tortoise_orm(new_city)


async def delete_city(*, city_id: UUID) -> None:
    city = await get_city_by_id(city_id=city_id)
    await city.delete()


async def get_city_by_id(*, city_id: UUID) -> City:
    try:
        city = await City.get(id=city_id)
        return city
    except DoesNotExist:
        logger.error(f' :: get_city_by_id :: city with id {city_id} not found')
        raise DoesNotExist('The city doesn\'t exist')
