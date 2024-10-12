from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def quote_cart_management_v1_create_empty_cart_post(request: web.Request, ) -> web.Response:
    """carts/

    Creates an empty cart and quote for a guest.


    """
    return web.Response(status=200)
