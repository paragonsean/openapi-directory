from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_billing_address_management_v1_assign_post_request import QuoteBillingAddressManagementV1AssignPostRequest
from openapi_server.models.quote_data_address_interface import QuoteDataAddressInterface
from openapi_server import util


async def quote_guest_billing_address_management_v1_assign_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/billing-address

    Assign a specified billing address to a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteBillingAddressManagementV1AssignPostRequest.from_dict(body)
    return web.Response(status=200)


async def quote_guest_billing_address_management_v1_get_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/billing-address

    Return the billing address for a specified quote.

    :param cart_id: The cart ID.
    :type cart_id: str

    """
    return web.Response(status=200)
