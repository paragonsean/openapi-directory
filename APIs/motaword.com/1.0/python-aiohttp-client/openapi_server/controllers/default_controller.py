from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def delete_cache(request: web.Request, key) -> web.Response:
    """Clear cache by key

    

    :param key: Cache key
    :type key: str

    """
    return web.Response(status=200)
