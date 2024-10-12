from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def admin(request: web.Request, ) -> web.Response:
    """admin

    Ping the server


    """
    return web.Response(status=200)


async def log_in_ritc(request: web.Request, message) -> web.Response:
    """log_in_ritc

    Log a message

    :param message: Log message
    :type message: 

    """
    return web.Response(status=200)


async def ping_ritc(request: web.Request, ) -> web.Response:
    """ping_ritc

    Ping the server


    """
    return web.Response(status=200)
