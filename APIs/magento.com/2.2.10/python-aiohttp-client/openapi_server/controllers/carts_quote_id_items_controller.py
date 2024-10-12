from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface
from openapi_server import util


async def v1_carts_quote_id_items_post(request: web.Request, quote_id, body=None) -> web.Response:
    """carts/{quoteId}/items

    Add/update the specified cart item.

    :param quote_id: 
    :type quote_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartItemRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
