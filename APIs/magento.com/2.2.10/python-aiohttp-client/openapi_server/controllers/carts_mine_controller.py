from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_repository_v1_save_put_request import QuoteCartRepositoryV1SavePutRequest
from openapi_server.models.quote_data_cart_interface import QuoteDataCartInterface
from openapi_server import util


async def quote_cart_management_v1_create_empty_cart_for_customer_post(request: web.Request, ) -> web.Response:
    """carts/mine

    Creates an empty cart and quote for a specified customer if customer does not have a cart yet.


    """
    return web.Response(status=200)


async def quote_cart_management_v1_get_cart_for_customer_get(request: web.Request, ) -> web.Response:
    """carts/mine

    Returns information for the cart for a specified customer.


    """
    return web.Response(status=200)


async def quote_cart_repository_v1_save_put(request: web.Request, body=None) -> web.Response:
    """carts/mine

    Save quote

    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
