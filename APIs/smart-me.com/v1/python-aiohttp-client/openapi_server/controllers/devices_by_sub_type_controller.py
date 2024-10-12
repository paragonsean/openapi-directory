from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server import util


async def devices_by_sub_type_get(request: web.Request, meter_sub_type) -> web.Response:
    """Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)

    Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)

    :param meter_sub_type: 
    :type meter_sub_type: str

    """
    return web.Response(status=200)
