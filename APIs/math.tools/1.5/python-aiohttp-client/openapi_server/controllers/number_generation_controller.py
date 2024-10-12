from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_random_get(request: web.Request, min=None, max=None, total=None) -> web.Response:
    """numbers_random_get

    Generate random number(s)

    :param min: Minimum Number value in the range
    :type min: int
    :param max: Maximum Number value
    :type max: int
    :param total: Total number of random numbers to generate. Defaults to 1
    :type total: int

    """
    return web.Response(status=200)
