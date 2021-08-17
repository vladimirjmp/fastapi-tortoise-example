from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from tortoise.exceptions import DoesNotExist


def register_exception_handlers(app):

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ) -> JSONResponse:
        errors = [
            dict(
                code=error.get('type').split('.')[-1],
                field=error.get('loc')[-1],
                message=error.get('msg').capitalize()
            )
            for error in exc.errors()
        ]
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'errors': errors
            },
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request,
        exc: StarletteHTTPException
    ):
        errors = [
            dict(
                code='error',
                message=exc.detail
            )
        ]
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'errors': errors
            },
        )

    @app.exception_handler(DoesNotExist)
    async def not_exists_exception_handler(
        request: Request,
        exc: DoesNotExist
    ):
        errors = [
            dict(
                code='not_found',
                message=str(exc)
            )
        ]
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                'errors': errors
            },
        )
