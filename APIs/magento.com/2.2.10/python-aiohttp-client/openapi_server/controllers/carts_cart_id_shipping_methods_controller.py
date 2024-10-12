from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server import util


async def v1_carts_cart_id_shipping_methods_get(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}/shipping-methods

    Lists applicable shipping methods for a specified quote.

    :param cart_id: The shopping cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)
