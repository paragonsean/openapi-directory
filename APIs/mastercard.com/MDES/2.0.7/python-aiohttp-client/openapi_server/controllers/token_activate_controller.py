from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_activate_request_schema import TokenActivateRequestSchema
from openapi_server.models.token_activate_response_schema import TokenActivateResponseSchema
from openapi_server import util


async def token_activate_post(request: web.Request, token_activate_request_schema=None) -> web.Response:
    """token_activate_post

    Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation. If the provisioning was not completed successfully, activation cannot be accomplished using Customer Service API. It is expected that a cardholder will complete the authentication process using an issuer&#39;s call center or using an issuer-supplied mobile application, and only then should the issuer use this API to activate the token. 

    :param token_activate_request_schema: Contains the details of the request message.
    :type token_activate_request_schema: dict | bytes

    """
    token_activate_request_schema = TokenActivateRequestSchema.from_dict(token_activate_request_schema)
    return web.Response(status=200)
