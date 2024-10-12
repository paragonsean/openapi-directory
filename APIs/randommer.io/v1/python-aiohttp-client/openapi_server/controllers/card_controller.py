from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_card_get(request: web.Request, type=None, x_api_key=None) -> web.Response:
    """Get Card

    

    :param type: 
    :type type: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_card_types_get(request: web.Request, x_api_key=None) -> web.Response:
    """Get available card types

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)
