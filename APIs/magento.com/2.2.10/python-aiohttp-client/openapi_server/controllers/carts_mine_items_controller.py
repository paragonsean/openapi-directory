from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface
from openapi_server import util


async def quote_cart_item_repository_v1_get_list_get(request: web.Request, ) -> web.Response:
    """carts/mine/items

    Lists items that are assigned to a specified cart.


    """
    return web.Response(status=200)


async def quote_cart_item_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/items

    Add/update the specified cart item.

    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartItemRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
