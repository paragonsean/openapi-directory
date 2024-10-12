from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_lldp_cdp_1(request: web.Request, serial) -> web.Response:
    """List LLDP and CDP information for a device

    List LLDP and CDP information for a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
