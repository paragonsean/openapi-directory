from typing import List, Dict
from aiohttp import web

from openapi_server.models.redirect import Redirect
from openapi_server.models.tokens_get_ephemeral_token_response_body_yaml import TokensGetEphemeralTokenResponseBodyYaml
from openapi_server import util


async def tokens_get_ephemeral_token(request: web.Request, redirect=None) -> web.Response:
    """Get Ephemeral Token

    This endpoint returns a token that can be passed to an application for authorized access.  The lifetime of this token is 10 seconds.

    :param redirect: Include a redirect url to the application formatted with the ephemeral token.
    :type redirect: dict | bytes

    """
    redirect = .from_dict(redirect)
    return web.Response(status=200)
