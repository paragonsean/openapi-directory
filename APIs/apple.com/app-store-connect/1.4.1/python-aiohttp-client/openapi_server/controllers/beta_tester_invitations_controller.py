from typing import List, Dict
from aiohttp import web

from openapi_server.models.beta_tester_invitation_create_request import BetaTesterInvitationCreateRequest
from openapi_server.models.beta_tester_invitation_response import BetaTesterInvitationResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_tester_invitations_create_instance(request: web.Request, body) -> web.Response:
    """beta_tester_invitations_create_instance

    

    :param body: BetaTesterInvitation representation
    :type body: dict | bytes

    """
    body = BetaTesterInvitationCreateRequest.from_dict(body)
    return web.Response(status=200)
