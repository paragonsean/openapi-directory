from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_credentials import AccessTokenCredentials
from openapi_server.models.client_credentials import ClientCredentials
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.public_authentication_output_model import PublicAuthenticationOutputModel
from openapi_server import util


async def heart_beat_get_authorization(request: web.Request, ) -> web.Response:
    """Returns http status code 204 for successful authentication.

    This route requires authentication, returns 204 http status when successful.


    """
    return web.Response(status=200)


async def heart_beat_get_database_status(request: web.Request, ) -> web.Response:
    """Can be used to check the status of the database.

    This does not require authentication.


    """
    return web.Response(status=200)


async def heart_beat_get_server_status(request: web.Request, ) -> web.Response:
    """Can be used to check the status of the REST Api.

    This does not require authentication.


    """
    return web.Response(status=200)


async def public_bearer_authentication_get_access_token_json(request: web.Request, body=None) -> web.Response:
    """Get oAuth2 access token.

    

    :param body: AccessTokenCredentials model
    :type body: dict | bytes

    """
    body = AccessTokenCredentials.from_dict(body)
    return web.Response(status=200)


async def public_bearer_authentication_get_access_token_token_from_refresh_token(request: web.Request, body=None) -> web.Response:
    """Get new access token using a refresh token.

    

    :param body: Refresh token.
    :type body: str

    """
    return web.Response(status=200)


async def public_bearer_authentication_get_authorization_code(request: web.Request, response_type=None, state=None, client_id=None, redirect_uri=None, scope=None) -> web.Response:
    """Get the oAuth2 authorization code flow code.

    

    :param response_type: code
    :type response_type: str
    :param state: Unguessable random string.
    :type state: str
    :param client_id: Client id.
    :type client_id: str
    :param redirect_uri: Url where to redirect after code has been retrieved.
    :type redirect_uri: str
    :param scope: Scopes that client requests. If scopes that are not allowed for the client are requested, returns unauthorized.
    :type scope: str

    """
    return web.Response(status=200)


async def public_bearer_authentication_get_login_token(request: web.Request, body=None) -> web.Response:
    """Can be used to get the login information and access token for the api client.

    

    :param body: ClientCredentials of the client.
    :type body: dict | bytes

    """
    body = ClientCredentials.from_dict(body)
    return web.Response(status=200)


async def public_bearer_authentication_logout(request: web.Request, body=None) -> web.Response:
    """Logout. Invalidates refresh token. Access token will be invalid when it expires.

    

    :param body: 
    :type body: str

    """
    return web.Response(status=200)
