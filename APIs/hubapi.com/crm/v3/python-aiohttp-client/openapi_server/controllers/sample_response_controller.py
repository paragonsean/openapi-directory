from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.integrator_card_payload_response import IntegratorCardPayloadResponse
from openapi_server import util


async def get_crm_v3_extensions_cards_sample_response(request: web.Request, ) -> web.Response:
    """Get sample card detail response

    Returns an example card detail response. This is the payload with displayed details for a card that will be shown to a user. An app should send this in response to the data fetch request.


    """
    return web.Response(status=200)
