from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface
from openapi_server import util


async def quote_cart_total_repository_v1_get_get(request: web.Request, ) -> web.Response:
    """carts/mine/totals

    Returns quote totals data for a specified cart.


    """
    return web.Response(status=200)
