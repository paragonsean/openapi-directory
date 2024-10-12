from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface
from openapi_server import util


async def v1_carts_cart_id_totals_get(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}/totals

    Returns quote totals data for a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)
