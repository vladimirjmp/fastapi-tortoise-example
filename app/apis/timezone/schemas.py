from pydantic import BaseModel, Field


class City(BaseModel):
    name: str = Field(
        ...,
        description='The name of the City',
        example='Lima'
    )
    timezone: str = Field(
        ...,
        description='The timezone of the city',
        example='America/Lima'
    )


class CityTime(City):
    current_time: str = Field(
        ...,
        description='The current time of the city',
        example='2021-08-09T10:39:32.991661-05:00'
    )
