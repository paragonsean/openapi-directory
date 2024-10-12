from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def fast_send_device_values_get(request: web.Request, id) -> web.Response:
    """Force a device to send the data every second (if supported). This for about 30s.              Don&#39;t use this call to force a device to send the data every second for a longer time.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
