from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_card_request import CreateCardRequest
from openapi_server.models.create_card_response import CreateCardResponse
from openapi_server.models.disable_card_response import DisableCardResponse
from openapi_server.models.list_cards_response import ListCardsResponse
from openapi_server.models.retrieve_card_response import RetrieveCardResponse
from openapi_server import util


async def create_card(request: web.Request, body) -> web.Response:
    """CreateCard

    Adds a card on file to an existing merchant.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateCardRequest.from_dict(body)
    return web.Response(status=200)


async def disable_card(request: web.Request, card_id) -> web.Response:
    """DisableCard

    Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed but has no effect.

    :param card_id: Unique ID for the desired Card.
    :type card_id: str

    """
    return web.Response(status=200)


async def list_cards(request: web.Request, cursor=None, customer_id=None, include_disabled=None, reference_id=None, sort_order=None) -> web.Response:
    """ListCards

    Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    :type cursor: str
    :param customer_id: Limit results to cards associated with the customer supplied. By default, all cards owned by the merchant are returned.
    :type customer_id: str
    :param include_disabled: Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
    :type include_disabled: bool
    :param reference_id: Limit results to cards associated with the reference_id supplied.
    :type reference_id: str
    :param sort_order: Sorts the returned list by when the card was created with the specified order. This field defaults to ASC.
    :type sort_order: str

    """
    return web.Response(status=200)


async def retrieve_card(request: web.Request, card_id) -> web.Response:
    """RetrieveCard

    Retrieves details for a specific Card.

    :param card_id: Unique ID for the desired Card.
    :type card_id: str

    """
    return web.Response(status=200)
