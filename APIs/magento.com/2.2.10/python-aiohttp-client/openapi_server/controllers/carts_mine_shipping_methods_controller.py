from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server import util


async def quote_shipping_method_management_v1_get_list_get(request: web.Request, ) -> web.Response:
    """carts/mine/shipping-methods

    Lists applicable shipping methods for a specified quote.


    """
    return web.Response(status=200)
