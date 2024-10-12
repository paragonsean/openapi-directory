from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_misc_cultures_get(request: web.Request, x_api_key=None) -> web.Response:
    """api_misc_cultures_get

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_misc_random_address_get(request: web.Request, number, culture=None, x_api_key=None) -> web.Response:
    """api_misc_random_address_get

    

    :param number: 
    :type number: int
    :param culture: 
    :type culture: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)
