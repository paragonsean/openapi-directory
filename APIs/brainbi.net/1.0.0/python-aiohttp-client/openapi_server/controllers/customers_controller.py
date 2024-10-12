from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def customers(request: web.Request, =None) -> web.Response:
    """Customers

    This resource lists all cusomters that are currently saved in your account.

    :param : 
    :type : str

    """
    return web.Response(status=200)
