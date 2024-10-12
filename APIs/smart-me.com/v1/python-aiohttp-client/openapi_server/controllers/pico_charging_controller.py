from typing import List, Dict
from aiohttp import web

from openapi_server.models.pico_charging_data import PicoChargingData
from openapi_server import util


async def pico_charging_get(request: web.Request, id) -> web.Response:
    """Gets the active charging data of a pico station

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
