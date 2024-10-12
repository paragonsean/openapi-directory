from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def quotes_get_1(request: web.Request, ) -> web.Response:
    """Get quotes for all symbols

    Get quotes


    """
    return web.Response(status=200)


async def symbols_get_1(request: web.Request, ) -> web.Response:
    """Get a list of symbols for which we provide real-time quotes

    Symbol List


    """
    return web.Response(status=200)
