from typing import List, Dict
from aiohttp import web

from openapi_server.models.values_data import ValuesData
from openapi_server import util


async def values_get(request: web.Request, id) -> web.Response:
    """Gets all (last) values of a device

    

    :param id: The ID of the device
    :type id: str

    """
    return web.Response(status=200)
