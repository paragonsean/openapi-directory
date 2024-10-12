from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def quote_coupon_management_v1_get_get(request: web.Request, ) -> web.Response:
    """carts/mine/coupons

    Returns information for a coupon in a specified cart.


    """
    return web.Response(status=200)


async def quote_coupon_management_v1_remove_delete(request: web.Request, ) -> web.Response:
    """carts/mine/coupons

    Deletes a coupon from a specified cart.


    """
    return web.Response(status=200)
