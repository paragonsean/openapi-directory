from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server import util


async def device_by_serial_get(request: web.Request, serial) -> web.Response:
    """Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.

    Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.

    :param serial: The Serial Number of the device
    :type serial: int

    """
    return web.Response(status=200)
