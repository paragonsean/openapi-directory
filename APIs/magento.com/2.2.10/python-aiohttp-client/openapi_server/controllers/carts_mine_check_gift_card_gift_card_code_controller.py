from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def gift_card_account_gift_card_account_management_v1_check_gift_card_get(request: web.Request, gift_card_code) -> web.Response:
    """carts/mine/checkGiftCard/{giftCardCode}

    

    :param gift_card_code: 
    :type gift_card_code: str

    """
    return web.Response(status=200)
