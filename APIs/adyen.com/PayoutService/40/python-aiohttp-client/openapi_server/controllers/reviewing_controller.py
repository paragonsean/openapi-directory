from typing import List, Dict
from aiohttp import web

from openapi_server.models.modify_request import ModifyRequest
from openapi_server.models.modify_response import ModifyResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_confirm_third_party(request: web.Request, body=None) -> web.Response:
    """Confirm a payout

    Confirms a previously submitted payout.  To cancel a payout, use the &#x60;/declineThirdParty&#x60; endpoint.

    :param body: 
    :type body: dict | bytes

    """
    body = ModifyRequest.from_dict(body)
    return web.Response(status=200)


async def post_decline_third_party(request: web.Request, body=None) -> web.Response:
    """Cancel a payout

    Cancels a previously submitted payout.  To confirm and send a payout, use the &#x60;/confirmThirdParty&#x60; endpoint.

    :param body: 
    :type body: dict | bytes

    """
    body = ModifyRequest.from_dict(body)
    return web.Response(status=200)
