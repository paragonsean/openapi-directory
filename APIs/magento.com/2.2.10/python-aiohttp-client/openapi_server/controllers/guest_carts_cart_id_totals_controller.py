from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface
from openapi_server import util


async def quote_guest_cart_total_repository_v1_get_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/totals

    Return quote totals data for a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: str

    """
    return web.Response(status=200)
