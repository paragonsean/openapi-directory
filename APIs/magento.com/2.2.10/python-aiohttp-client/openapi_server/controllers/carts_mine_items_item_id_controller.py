from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface
from openapi_server import util


async def quote_cart_item_repository_v1_delete_by_id_delete(request: web.Request, item_id) -> web.Response:
    """carts/mine/items/{itemId}

    Removes the specified item from the specified cart.

    :param item_id: The item ID of the item to be removed.
    :type item_id: int

    """
    return web.Response(status=200)


async def quote_cart_item_repository_v1_save_put(request: web.Request, item_id, body=None) -> web.Response:
    """carts/mine/items/{itemId}

    Add/update the specified cart item.

    :param item_id: 
    :type item_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartItemRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
