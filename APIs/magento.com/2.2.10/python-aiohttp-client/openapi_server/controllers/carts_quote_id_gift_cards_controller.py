from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_card_account_data_gift_card_account_interface import GiftCardAccountDataGiftCardAccountInterface
from openapi_server import util


async def gift_card_account_gift_card_account_management_v1_get_list_by_quote_id_get(request: web.Request, quote_id) -> web.Response:
    """carts/{quoteId}/giftCards

    Return GiftCard Account cards

    :param quote_id: 
    :type quote_id: int

    """
    return web.Response(status=200)
