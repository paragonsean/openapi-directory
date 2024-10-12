from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def payment_methods_get(request: web.Request, ) -> web.Response:
    """Get list of payment methods

    Get list of payment methods


    """
    return web.Response(status=200)
