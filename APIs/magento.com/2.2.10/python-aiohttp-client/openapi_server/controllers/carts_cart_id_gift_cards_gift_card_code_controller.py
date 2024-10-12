from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def v1_carts_cart_id_gift_cards_gift_card_code_delete(request: web.Request, cart_id, gift_card_code) -> web.Response:
    """carts/{cartId}/giftCards/{giftCardCode}

    Remove GiftCard Account entity

    :param cart_id: 
    :type cart_id: int
    :param gift_card_code: 
    :type gift_card_code: str

    """
    return web.Response(status=200)
