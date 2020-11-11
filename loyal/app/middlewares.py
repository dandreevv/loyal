import logging
from typing import Callable, Awaitable

from aiohttp import web
from aiohttp.web_exceptions import HTTPClientError

from .responses import server_error, error

__all__ = ("register_middlewares",)

Handler = Callable[[web.Request], Awaitable[web.StreamResponse]]

logger = logging.getLogger("app")


@web.middleware
async def default_handler_middleware(
    request: web.Request,
    handler: Handler,
) -> web.StreamResponse:
    try:
        return await handler(request)
    except Exception as e:
        message = f"Caught unhandled exception - {e.__class__.__name__}: {e}"
        logger.error(message)
        return server_error()


@web.middleware
async def client_error_handler_middleware(
    request: web.Request,
    handler: Handler,
) -> web.StreamResponse:
    try:
        return await handler(request)
    except HTTPClientError as e:
        message = f"Client error - {e.status}: {e.reason}"
        logger.error(message)
        return error(e.status, e.reason)


def register_middlewares(app: web.Application) -> None:
    app.middlewares.append(default_handler_middleware)
    app.middlewares.append(client_error_handler_middleware)