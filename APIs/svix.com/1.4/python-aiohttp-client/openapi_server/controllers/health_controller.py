from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def health_api_v1_health_get(request: web.Request, idempotency_key=None) -> web.Response:
    """Health

    Verify the API server is up and running.

    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)
