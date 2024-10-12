from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface
from openapi_server import util


async def v1_carts_cart_id_items_item_id_delete(request: web.Request, cart_id, item_id) -> web.Response:
    """carts/{cartId}/items/{itemId}

    Removes the specified item from the specified cart.

    :param cart_id: The cart ID.
    :type cart_id: int
    :param item_id: The item ID of the item to be removed.
    :type item_id: int

    """
    return web.Response(status=200)


async def v1_carts_cart_id_items_item_id_put(request: web.Request, cart_id, item_id, body=None) -> web.Response:
    """carts/{cartId}/items/{itemId}

    Add/update the specified cart item.

    :param cart_id: 
    :type cart_id: str
    :param item_id: 
    :type item_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartItemRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
