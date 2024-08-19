from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server import util


async def configuration_delete(request: web.Request, key) -> web.Response:
    """Delete a configuration item.

    

    :param key: The key of the configuration item to remove.
    :type key: str

    """
    return web.Response(status=200)


async def configuration_get(request: web.Request, key) -> web.Response:
    """Get the value of a configuration item.

    The response content may vary based on the configuration item&#39;s data type.

    :param key: The key of the configuration item.
    :type key: str

    """
    return web.Response(status=200)


async def configuration_list(request: web.Request, ) -> web.Response:
    """Get the current system configuration.

    


    """
    return web.Response(status=200)
