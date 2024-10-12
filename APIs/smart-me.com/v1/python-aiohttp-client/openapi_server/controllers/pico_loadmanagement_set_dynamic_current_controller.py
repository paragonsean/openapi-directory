from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def pico_loadmanagement_set_dynamic_current_post(request: web.Request, serial, current) -> web.Response:
    """Sets the dynamic current of a load management group or a single station.

    

    :param serial: The serial number can be any pico serial in the group (e.g. 700001)
    :type serial: int
    :param current: The dynamic current of the group (in mA)
    :type current: int

    """
    return web.Response(status=200)
