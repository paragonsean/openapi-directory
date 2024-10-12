from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_message_cart_repository_v1_save_post_request import GiftMessageCartRepositoryV1SavePostRequest
from openapi_server.models.gift_message_data_message_interface import GiftMessageDataMessageInterface
from openapi_server import util


async def gift_message_guest_item_repository_v1_get_get(request: web.Request, cart_id, item_id) -> web.Response:
    """guest-carts/{cartId}/gift-message/{itemId}

    Return the gift message for a specified item in a specified shopping cart.

    :param cart_id: The shopping cart ID.
    :type cart_id: str
    :param item_id: The item ID.
    :type item_id: int

    """
    return web.Response(status=200)


async def gift_message_guest_item_repository_v1_save_post(request: web.Request, cart_id, item_id, body=None) -> web.Response:
    """guest-carts/{cartId}/gift-message/{itemId}

    Set the gift message for a specified item in a specified shopping cart.

    :param cart_id: The cart ID.
    :type cart_id: str
    :param item_id: The item ID.
    :type item_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GiftMessageCartRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
