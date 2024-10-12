from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_management_v1_place_order_put_request import QuoteCartManagementV1PlaceOrderPutRequest
from openapi_server import util


async def quote_cart_management_v1_place_order_put(request: web.Request, body=None) -> web.Response:
    """carts/mine/order

    Places an order for a specified cart.

    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartManagementV1PlaceOrderPutRequest.from_dict(body)
    return web.Response(status=200)
