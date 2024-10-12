from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def quote_guest_cart_management_v1_create_empty_cart_post(request: web.Request, ) -> web.Response:
    """guest-carts

    Enable an customer or guest user to create an empty cart and quote for an anonymous customer.


    """
    return web.Response(status=200)
