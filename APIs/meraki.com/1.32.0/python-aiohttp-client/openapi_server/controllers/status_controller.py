from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_wireless_status_1(request: web.Request, serial) -> web.Response:
    """Return the SSID statuses of an access point

    Return the SSID statuses of an access point

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
