from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def download_async(request: web.Request, async_request_key) -> web.Response:
    """Download result of an async operation

    Download the result of an async operation that you have requested in other endpoints.

    :param async_request_key: Async operation key
    :type async_request_key: str

    """
    return web.Response(status=200)
