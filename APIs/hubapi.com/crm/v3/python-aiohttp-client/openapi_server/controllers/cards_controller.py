from typing import List, Dict
from aiohttp import web

from openapi_server.models.card_create_request import CardCreateRequest
from openapi_server.models.card_list_response import CardListResponse
from openapi_server.models.card_patch_request import CardPatchRequest
from openapi_server.models.card_response import CardResponse
from openapi_server.models.error import Error
from openapi_server import util


async def delete_crm_v3_extensions_cards_app_id_card_id(request: web.Request, app_id, card_id) -> web.Response:
    """Delete a card

    Permanently deletes a card definition with the given ID. Once deleted, data fetch requests for this card will no longer be sent to your service. This can&#39;t be undone.

    :param app_id: The ID of the target app.
    :type app_id: int
    :param card_id: The ID of the card to delete.
    :type card_id: str

    """
    return web.Response(status=200)


async def get_crm_v3_extensions_cards_app_id(request: web.Request, app_id) -> web.Response:
    """Get all cards

    Returns a list of cards for a given app.

    :param app_id: The ID of the target app.
    :type app_id: int

    """
    return web.Response(status=200)


async def get_crm_v3_extensions_cards_app_id_card_id(request: web.Request, app_id, card_id) -> web.Response:
    """Get a card.

    Returns the definition for a card with the given ID.

    :param app_id: The ID of the target app.
    :type app_id: int
    :param card_id: The ID of the target card.
    :type card_id: str

    """
    return web.Response(status=200)


async def patch_crm_v3_extensions_cards_app_id_card_id(request: web.Request, app_id, card_id, body) -> web.Response:
    """Update a card

    Update a card definition with new details.

    :param app_id: The ID of the target app.
    :type app_id: int
    :param card_id: The ID of the card to update.
    :type card_id: str
    :param body: Card definition fields to be updated.
    :type body: dict | bytes

    """
    body = CardPatchRequest.from_dict(body)
    return web.Response(status=200)


async def post_crm_v3_extensions_cards_app_id(request: web.Request, app_id, body) -> web.Response:
    """Create a new card

    Defines a new card that will become active on an account when this app is installed.

    :param app_id: The ID of the target app.
    :type app_id: int
    :param body: The new card definition.
    :type body: dict | bytes

    """
    body = CardCreateRequest.from_dict(body)
    return web.Response(status=200)
