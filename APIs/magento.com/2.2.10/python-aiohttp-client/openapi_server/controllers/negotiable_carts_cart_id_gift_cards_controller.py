from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_card_account_guest_gift_card_account_management_v1_add_gift_card_post_request import GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest
from openapi_server import util


async def negotiable_quote_gift_card_account_management_v1_save_by_quote_id_post(request: web.Request, cart_id, body=None) -> web.Response:
    """negotiable-carts/{cartId}/giftCards

    

    :param cart_id: 
    :type cart_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest.from_dict(body)
    return web.Response(status=200)
