from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_billing_address_management_v1_assign_post_request import QuoteBillingAddressManagementV1AssignPostRequest
from openapi_server.models.quote_data_address_interface import QuoteDataAddressInterface
from openapi_server import util


async def quote_billing_address_management_v1_assign_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/billing-address

    Assigns a specified billing address to a specified cart.

    :param body: 
    :type body: dict | bytes

    """
    body = QuoteBillingAddressManagementV1AssignPostRequest.from_dict(body)
    return web.Response(status=200)


async def quote_billing_address_management_v1_get_get(request: web.Request, ) -> web.Response:
    """carts/mine/billing-address

    Returns the billing address for a specified quote.


    """
    return web.Response(status=200)
