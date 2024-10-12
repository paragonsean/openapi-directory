from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.authenticate_payload import AuthenticatePayload
from openapi_server.models.bad_request import BadRequest
from openapi_server.models.refresh_token_payload import RefreshTokenPayload
from openapi_server import util


async def p_ost_auth_api_key(request: web.Request, body=None) -> web.Response:
    """Authenticate

    To get started, submit your API key in the body of your request. api.video returns an access token that is valid for one hour (3600 seconds). A refresh token is also returned. View a [tutorial](https://api.video/blog/tutorials/authentication-tutorial) on authentication. All tutorials using the [authentication endpoint](https://api.video/blog/endpoints/authenticate)

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatePayload.from_dict(body)
    return web.Response(status=200)


async def p_ost_auth_refresh(request: web.Request, body=None) -> web.Response:
    """Refresh token

    Use the refresh endpoint with the refresh token you received when you first authenticated using the api-key endpoint. Send the refresh token in the body of your request. The api.video API returns a new access token that is valid for one hour (3600 seconds) and a new refresh token.  

    :param body: 
    :type body: dict | bytes

    """
    body = RefreshTokenPayload.from_dict(body)
    return web.Response(status=200)
