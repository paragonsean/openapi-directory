from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server import util


async def virtual_billing_meters_get(request: web.Request, ) -> web.Response:
    """Beta: Gets all Meters available to activate as a Virtual Meter.

    Beta: Gets all Meters available to activate as a Virtual Meter.


    """
    return web.Response(status=200)
