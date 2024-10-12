from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def negotiable_quote_coupon_management_v1_remove_delete(request: web.Request, cart_id) -> web.Response:
    """negotiable-carts/{cartId}/coupons

    Deletes a coupon from a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)
