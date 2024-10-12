from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_payment_interface import QuoteDataPaymentInterface
from openapi_server.models.quote_payment_method_management_v1_set_put_request import QuotePaymentMethodManagementV1SetPutRequest
from openapi_server import util


async def quote_payment_method_management_v1_get_get(request: web.Request, ) -> web.Response:
    """carts/mine/selected-payment-method

    Returns the payment method for a specified shopping cart.


    """
    return web.Response(status=200)


async def quote_payment_method_management_v1_set_put(request: web.Request, body=None) -> web.Response:
    """carts/mine/selected-payment-method

    Adds a specified payment method to a specified shopping cart.

    :param body: 
    :type body: dict | bytes

    """
    body = QuotePaymentMethodManagementV1SetPutRequest.from_dict(body)
    return web.Response(status=200)
