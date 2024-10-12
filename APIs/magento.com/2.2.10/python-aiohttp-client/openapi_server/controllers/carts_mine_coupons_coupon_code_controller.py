from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def quote_coupon_management_v1_set_put(request: web.Request, coupon_code) -> web.Response:
    """carts/mine/coupons/{couponCode}

    Adds a coupon by code to a specified cart.

    :param coupon_code: The coupon code data.
    :type coupon_code: str

    """
    return web.Response(status=200)
