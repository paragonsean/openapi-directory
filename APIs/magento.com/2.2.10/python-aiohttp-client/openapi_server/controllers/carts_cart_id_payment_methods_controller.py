from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_payment_method_interface import QuoteDataPaymentMethodInterface
from openapi_server import util


async def v1_carts_cart_id_payment_methods_get(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}/payment-methods

    Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

    :param cart_id: The cart ID.
    :type cart_id: int

    """
    return web.Response(status=200)
