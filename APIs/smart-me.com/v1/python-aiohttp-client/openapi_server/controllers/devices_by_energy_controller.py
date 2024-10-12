from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server import util


async def devices_by_energy_get(request: web.Request, meter_energy_type) -> web.Response:
    """Gets all Devices for an Energy Type

    Gets all Devices for an Energy Type

    :param meter_energy_type: 
    :type meter_energy_type: str

    """
    return web.Response(status=200)
