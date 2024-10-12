from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_management_v1_assign_customer_put_request import QuoteCartManagementV1AssignCustomerPutRequest
from openapi_server.models.quote_data_cart_interface import QuoteDataCartInterface
from openapi_server import util


async def quote_cart_management_v1_assign_customer_put(request: web.Request, cart_id, body=None) -> web.Response:
    """carts/{cartId}

    Assigns a specified customer to a specified shopping cart.

    :param cart_id: The cart ID.
    :type cart_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartManagementV1AssignCustomerPutRequest.from_dict(body)
    return web.Response(status=200)


async def quote_cart_repository_v1_get_get(request: web.Request, cart_id) -> web.Response:
    """carts/{cartId}

    Enables an administrative user to return information for a specified cart.

    :param cart_id: 
    :type cart_id: int

    """
    return web.Response(status=200)
