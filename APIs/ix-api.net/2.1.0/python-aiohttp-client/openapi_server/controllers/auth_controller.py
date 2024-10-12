from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.auth_token import AuthToken
from openapi_server.models.auth_token_refresh401_response import AuthTokenRefresh401Response
from openapi_server.models.auth_token_request import AuthTokenRequest
from openapi_server.models.refresh_token_request import RefreshTokenRequest
from openapi_server import util


async def auth_token_create(request: web.Request, body=None) -> web.Response:
    """auth_token_create

    Authenticate an API user identified by &#x60;api_key&#x60; and &#x60;api_secret&#x60;.

    :param body: AuthTokenRequest
    :type body: dict | bytes

    """
    body = AuthTokenRequest.from_dict(body)
    return web.Response(status=200)


async def auth_token_refresh(request: web.Request, body=None) -> web.Response:
    """auth_token_refresh

    Reauthenticate the API user, issue a new &#x60;access_token&#x60; and &#x60;refresh_token&#x60; pair by providing the &#x60;refresh_token&#x60; in the request body.

    :param body: RefreshTokenRequest
    :type body: dict | bytes

    """
    body = RefreshTokenRequest.from_dict(body)
    return web.Response(status=200)
