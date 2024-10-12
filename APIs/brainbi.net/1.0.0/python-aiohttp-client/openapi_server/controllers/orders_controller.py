from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def orders(request: web.Request, =None) -> web.Response:
    """Orders

    This resource lists all orders that are currently saved in your account.

    :param : 
    :type : str

    """
    return web.Response(status=200)


async def orders1(request: web.Request, =None) -> web.Response:
    """Orders

    Orders

    :param : 
    :type : str

    """
    return web.Response(status=200)
