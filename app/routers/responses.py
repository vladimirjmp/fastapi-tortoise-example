from fastapi import status

CREATE_CITY_RESPONSE = {
    status.HTTP_201_CREATED: {
        'description': 'City created successfully',
        'content': {
            'application/json': {
                'example': {
                    'id': '804fe738-f90e-4e63-9efa-cbcc11940ec9',
                    'name': 'Lima',
                    'timezone': 'America/Lima',
                    'current_time': '2021-08-09T10:39:32.991661-05:00'
                }
            }
        }
    }
}
