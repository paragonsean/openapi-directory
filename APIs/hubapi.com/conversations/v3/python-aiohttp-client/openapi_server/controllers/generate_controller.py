from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.identification_token_generation_request import IdentificationTokenGenerationRequest
from openapi_server.models.identification_token_response import IdentificationTokenResponse
from openapi_server import util


async def post_conversations_v3_visitor_identification_tokens_create_generate_token(request: web.Request, body) -> web.Response:
    """Generate a token

    Generates a new visitor identification token. This token will be unique every time this endpoint is called, even if called with the same email address. This token is temporary and will expire after 12 hours

    :param body: 
    :type body: dict | bytes

    """
    body = IdentificationTokenGenerationRequest.from_dict(body)
    return web.Response(status=200)
