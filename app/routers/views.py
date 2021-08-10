from typing import List
from uuid import UUID

from apis.timezone import services
from apis.timezone.models import City_Pydantic, CityIn_Pydantic
from fastapi import APIRouter, status
from routers import responses

router = APIRouter(
    prefix='/cities',
    tags=['cities']
)


@router.get('', response_model=List[City_Pydantic])
async def fetch_all_cities():
    return await services.get_cities()


@router.get('/{city_id}', response_model=City_Pydantic)
async def get_city(city_id: UUID):
    return await services.get_city(city_id=city_id)


@router.post(
    '',
    response_model=CityIn_Pydantic,
    status_code=status.HTTP_201_CREATED,
    responses={**responses.CREATE_CITY_RESPONSE},
    openapi_extra={
        "example": {
            "name": "Lima",
            "timezone": "America/Lima"
        }
    }
)
async def create_city(city: CityIn_Pydantic):
    """Service to create cities"""
    return await services.create_city(city=city)


@router.delete('/{city_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(city_id: UUID):
    await services.delete_city(city_id=city_id)
