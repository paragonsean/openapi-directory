from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def negotiable_quote_gift_card_account_management_v1_delete_by_quote_id_delete(request: web.Request, cart_id, gift_card_code) -> web.Response:
    """negotiable-carts/{cartId}/giftCards/{giftCardCode}

    Remove GiftCard Account entity

    :param cart_id: 
    :type cart_id: int
    :param gift_card_code: 
    :type gift_card_code: str

    """
    return web.Response(status=200)
