from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_appliance_dhcp_subnets_2(request: web.Request, serial) -> web.Response:
    """Return the DHCP subnet information for an appliance

    Return the DHCP subnet information for an appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
