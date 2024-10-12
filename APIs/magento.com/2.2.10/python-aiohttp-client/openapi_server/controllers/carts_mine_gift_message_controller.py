from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_message_cart_repository_v1_save_post_request import GiftMessageCartRepositoryV1SavePostRequest
from openapi_server.models.gift_message_data_message_interface import GiftMessageDataMessageInterface
from openapi_server import util


async def gift_message_cart_repository_v1_get_get(request: web.Request, ) -> web.Response:
    """carts/mine/gift-message

    Return the gift message for a specified order.


    """
    return web.Response(status=200)


async def gift_message_cart_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/gift-message

    Set the gift message for an entire order.

    :param body: 
    :type body: dict | bytes

    """
    body = GiftMessageCartRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
