from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_payment_method_interface import QuoteDataPaymentMethodInterface
from openapi_server import util


async def quote_payment_method_management_v1_get_list_get(request: web.Request, ) -> web.Response:
    """carts/mine/payment-methods

    Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.


    """
    return web.Response(status=200)
