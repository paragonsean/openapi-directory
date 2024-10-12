from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_appliance_performance_1(request: web.Request, serial) -> web.Response:
    """Return the performance score for a single MX

    Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
