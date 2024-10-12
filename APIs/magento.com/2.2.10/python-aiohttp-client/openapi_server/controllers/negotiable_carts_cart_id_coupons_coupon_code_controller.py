from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def negotiable_quote_coupon_management_v1_set_put(request: web.Request, cart_id, coupon_code) -> web.Response:
    """negotiable-carts/{cartId}/coupons/{couponCode}

    Adds a coupon by code to a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: int
    :param coupon_code: The coupon code data.
    :type coupon_code: str

    """
    return web.Response(status=200)
