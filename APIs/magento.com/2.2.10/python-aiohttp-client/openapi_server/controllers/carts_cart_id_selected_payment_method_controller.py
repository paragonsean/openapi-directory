from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_payment_interface import QuoteDataPaymentInterface
from openapi_server.models.quote_payment_method_management_v1_set_put_request import QuotePaymentMethodManagementV1SetPutRequest
from openapi_server import util


async def v1_carts_cart_id_selected_payment_method_get(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}/selected-payment-method

    Returns the payment method for a specified shopping cart.

    :param cart_id: The cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)


async def v1_carts_cart_id_selected_payment_method_put(request: web.Request, cart_id, body=None) -> web.Response:
    """carts/{cartId}/selected-payment-method

    Adds a specified payment method to a specified shopping cart.

    :param cart_id: The cart ID.
    :type cart_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = QuotePaymentMethodManagementV1SetPutRequest.from_dict(body)
    return web.Response(status=200)
