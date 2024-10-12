from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def pico_enable_fix_cable_lock_post(request: web.Request, id) -> web.Response:
    """Try to fix lock the cable of a pico. The pico must be online and a cable (without car) needs to be connected. Otherwise this will fail.

    

    :param id: The ID of the pico
    :type id: str

    """
    return web.Response(status=200)
