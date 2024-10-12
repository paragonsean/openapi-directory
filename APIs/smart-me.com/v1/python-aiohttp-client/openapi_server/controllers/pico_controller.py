from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server import util


async def pico_get(request: web.Request, ) -> web.Response:
    """Gets all pico charging stations for this user

    


    """
    return web.Response(status=200)
