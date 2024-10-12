from typing import List, Dict
from aiohttp import web

from openapi_server.models.gift_card import GiftCard
from openapi_server import util


async def get_gift_card_details(request: web.Request, ) -> web.Response:
    """Lists information on gift cards

    Returns images and details (and associated denominations) of all gift cards


    """
    return web.Response(status=200)


async def gift_card_details(request: web.Request, ) -> web.Response:
    """Lists information on gift cards

    Returns images and details (and associated denominations) of all gift cards


    """
    return web.Response(status=200)
