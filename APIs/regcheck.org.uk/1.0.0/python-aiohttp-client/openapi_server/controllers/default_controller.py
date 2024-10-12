from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def check(request: web.Request, search_string) -> web.Response:
    """Gets details of a UK Vehicle

    Gets details of a UK Vehicle 

    :param search_string: A registration number
    :type search_string: str

    """
    return web.Response(status=200)
