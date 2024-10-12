from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_management_v1_place_order_put_request import QuoteCartManagementV1PlaceOrderPutRequest
from openapi_server import util


async def quote_guest_cart_management_v1_place_order_put(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/order

    Place an order for a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartManagementV1PlaceOrderPutRequest.from_dict(body)
    return web.Response(status=200)
