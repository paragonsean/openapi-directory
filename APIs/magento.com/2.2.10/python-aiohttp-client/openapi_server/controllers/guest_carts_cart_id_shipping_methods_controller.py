from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server import util


async def quote_guest_shipping_method_management_v1_get_list_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/shipping-methods

    List applicable shipping methods for a specified quote.

    :param cart_id: The shopping cart ID.
    :type cart_id: str

    """
    return web.Response(status=200)
