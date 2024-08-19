from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_fact_get(request: web.Request, number) -> web.Response:
    """numbers_fact_get

    Get a random fact about a number

    :param number: Number value
    :type number: int

    """
    return web.Response(status=200)
