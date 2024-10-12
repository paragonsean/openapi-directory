from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface
from openapi_server import util


async def quote_guest_cart_item_repository_v1_get_list_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/items

    List items that are assigned to a specified cart.

    :param cart_id: The cart ID.
    :type cart_id: str

    """
    return web.Response(status=200)


async def quote_guest_cart_item_repository_v1_save_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/items

    Add/update the specified cart item.

    :param cart_id: 
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartItemRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
