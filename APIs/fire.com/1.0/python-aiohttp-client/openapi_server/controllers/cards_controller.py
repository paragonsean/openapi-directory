from typing import List, Dict
from aiohttp import web

from openapi_server.models.card_transactionsv1 import CardTransactionsv1
from openapi_server.models.cards import Cards
from openapi_server.models.new_card import NewCard
from openapi_server.models.new_card_response import NewCardResponse
from openapi_server import util


async def block_card(request: web.Request, card_id) -> web.Response:
    """Block a card

    Updates status of an existing card to block which prevents any transactions being carried out with that card.

    :param card_id: 
    :type card_id: int

    """
    return web.Response(status=200)


async def create_new_card(request: web.Request, body) -> web.Response:
    """Create a new debit card.

    You can create multiple debit cards which can be linked to your fire.com accounts.

    :param body: Details of the new card
    :type body: dict | bytes

    """
    body = NewCard.from_dict(body)
    return web.Response(status=200)


async def get_listof_card_transactions(request: web.Request, card_id, limit=None, offset=None) -> web.Response:
    """List Card Transactions.

    Returns a list of cards transactions related to your fire.com card.

    :param card_id: 
    :type card_id: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_listof_cards(request: web.Request, ) -> web.Response:
    """View List of Cards.

    Returns a list of cards related to your fire.com account.


    """
    return web.Response(status=200)


async def unblock_card(request: web.Request, card_id) -> web.Response:
    """Unblock a card

    Updates status of an existing card to unblock which means that transactions can be carried out with that card.

    :param card_id: 
    :type card_id: int

    """
    return web.Response(status=200)
