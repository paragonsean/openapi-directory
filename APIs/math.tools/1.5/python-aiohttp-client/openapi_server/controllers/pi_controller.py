from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_pi_get(request: web.Request, _from=None, to=None) -> web.Response:
    """numbers_pi_get

    Get digits of pi (Ï€)

    :param _from: Optional start position
    :type _from: int
    :param to: Optional start position
    :type to: int

    """
    return web.Response(status=200)
