from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth import Auth
from openapi_server.models.auth_error import AuthError
from openapi_server.models.client_auth_request import ClientAuthRequest
from openapi_server.models.convert_access_token_request import ConvertAccessTokenRequest
from openapi_server.models.error import Error
from openapi_server.models.exchange_auth_code_request import ExchangeAuthCodeRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def client_auth(request: web.Request, body) -> web.Response:
    """Authorize a client with OAuth

    For information on utilizing OAuth client authorization, see our [authentication](/api/authentication#generate-unauthenticated-tokens) documentation or the [Client Credentials Grant](https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4) section of the [OAuth spec](https://tools.ietf.org/html/draft-ietf-oauth-v2-31.

    :param body: 
    :type body: dict | bytes

    """
    body = ClientAuthRequest.from_dict(body)
    return web.Response(status=200)


async def convert_access_token(request: web.Request, body) -> web.Response:
    """Convert OAuth 1 access tokens to OAuth 2 access tokens

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConvertAccessTokenRequest.from_dict(body)
    return web.Response(status=200)


async def delete_token(request: web.Request, ) -> web.Response:
    """Revoke the current access token

    This method enables an app to notify the API that it is done with a token and that the token can be discarded.


    """
    return web.Response(status=200)


async def exchange_auth_code(request: web.Request, body) -> web.Response:
    """Exchange an authorization code for an access token

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExchangeAuthCodeRequest.from_dict(body)
    return web.Response(status=200)


async def verify_token(request: web.Request, ) -> web.Response:
    """Verify an OAuth 2 token

    


    """
    return web.Response(status=200)
