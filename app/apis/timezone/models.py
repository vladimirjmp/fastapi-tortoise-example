from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from utils.requests import get_current_time_sync


class City(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(
        50,
        unique=True,
        description='The name of the city'
    )
    timezone = fields.CharField(50)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def current_time(self) -> str:
        current_time = get_current_time_sync(self.timezone)
        return current_time

    class PydanticMeta:
        exclude = ('created_at', 'updated_at')
        computed = ('current_time',)

    class Meta:
        ordering = ['created_at']
        table = 'city'

    def __str__(self):
        return self.name


City_Pydantic = pydantic_model_creator(City, name='City')
CityIn_Pydantic_Base = pydantic_model_creator(
    City,
    name='CityIn',
    exclude_readonly=True
)


class CityIn_Pydantic(CityIn_Pydantic_Base):
    class Config:
        schema_extra = {
            "example": {
                "name": "Lima",
                "timezone": "America/Lima",
            }
        }
