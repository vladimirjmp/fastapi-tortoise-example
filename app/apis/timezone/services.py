from typing import Any, Dict
from uuid import UUID

from apis.timezone.models import City, City_Pydantic, CityIn_Pydantic


async def get_cities():
    return await City_Pydantic.from_queryset(City.all())


async def get_city(*, city_id: UUID) -> Dict[str, Any]:
    return await City_Pydantic.from_queryset_single(City.get(id=city_id))


async def create_city(*, city: CityIn_Pydantic) -> Dict[str, Any]:
    new_city = await City.create(**city.dict(exclude_unset=True))
    return await CityIn_Pydantic.from_tortoise_orm(new_city)


async def delete_city(*, city_id: UUID) -> None:
    await City.filter(id=city_id).delete()
