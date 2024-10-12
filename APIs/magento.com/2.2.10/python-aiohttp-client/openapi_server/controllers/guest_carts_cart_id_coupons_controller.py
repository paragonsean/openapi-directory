from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def quote_guest_coupon_management_v1_get_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/coupons

    Return information for a coupon in a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: str

    """
    return web.Response(status=200)


async def quote_guest_coupon_management_v1_remove_delete(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/coupons

    Delete a coupon from a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: str

    """
    return web.Response(status=200)
