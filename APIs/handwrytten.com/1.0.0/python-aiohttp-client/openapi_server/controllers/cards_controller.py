from typing import List, Dict
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.card_details import CardDetails
from openapi_server.models.filterable_card_details_request import FilterableCardDetailsRequest
from openapi_server.models.list_cards_request import ListCardsRequest
from openapi_server import util


async def filterable_card_details(request: web.Request, body=None) -> web.Response:
    """Provides full information on a specific card

    Full card details

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = FilterableCardDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def list_cards(request: web.Request, body=None) -> web.Response:
    """Lists information on cards

    Simple listing of cards.  No filters can be applied.

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = ListCardsRequest.from_dict(body)
    return web.Response(status=200)


async def simple_list_cards(request: web.Request, ) -> web.Response:
    """Lists information on cards

    Filterable card list.  If called with UID will also provide user-specific cards.


    """
    return web.Response(status=200)
