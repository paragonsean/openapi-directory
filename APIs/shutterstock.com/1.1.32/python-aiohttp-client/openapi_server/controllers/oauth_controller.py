from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_access_token_request import CreateAccessTokenRequest
from openapi_server.models.create_access_token_request1 import CreateAccessTokenRequest1
from openapi_server.models.oauth_access_token_response import OauthAccessTokenResponse
from openapi_server import util


async def authorize(request: web.Request, client_id, redirect_uri, response_type, state, realm=None, scope=None) -> web.Response:
    """Authorize applications

    This endpoint returns a redirect URI (in the &#39;Location&#39; header) that the customer uses to authorize your application and, together with POST /v2/oauth/access_token, generate an access token that represents that authorization.

    :param client_id: Client ID (Consumer Key) of your application
    :type client_id: str
    :param redirect_uri: The callback URI to send the request to after authorization; must use a host name that is registered with your application
    :type redirect_uri: str
    :param response_type: Type of temporary authorization code that will be used to generate an access code; the only valid value is &#39;code&#39;
    :type response_type: str
    :param state: Unique value used by the calling app to verify the request
    :type state: str
    :param realm: User type to be authorized (usually &#39;customer&#39;)
    :type realm: str
    :param scope: Space-separated list of scopes to be authorized
    :type scope: str

    """
    return web.Response(status=200)


async def create_access_token(request: web.Request, body=None) -> web.Response:
    """Get access tokens

    This endpoint returns an access token for the specified user and with the specified scopes. The token does not expire until the user changes their password. The body parameters must be encoded as form data.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccessTokenRequest.from_dict(body)
    return web.Response(status=200)
