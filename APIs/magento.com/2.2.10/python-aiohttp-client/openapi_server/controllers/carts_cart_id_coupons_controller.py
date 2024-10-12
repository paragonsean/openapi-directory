from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def v1_carts_cart_id_coupons_delete(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}/coupons

    Deletes a coupon from a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)


async def v1_carts_cart_id_coupons_get(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}/coupons

    Returns information for a coupon in a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)
