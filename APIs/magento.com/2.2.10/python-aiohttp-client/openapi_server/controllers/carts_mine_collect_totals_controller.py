from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_total_management_v1_collect_totals_put_request import QuoteCartTotalManagementV1CollectTotalsPutRequest
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface
from openapi_server import util


async def quote_cart_total_management_v1_collect_totals_put(request: web.Request, body=None) -> web.Response:
    """carts/mine/collect-totals

    Set shipping/billing methods and additional data for cart and collect totals.

    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartTotalManagementV1CollectTotalsPutRequest.from_dict(body)
    return web.Response(status=200)
