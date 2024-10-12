from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_access_token_response import GenerateAccessTokenResponse
from openapi_server import util


async def generate_token_v2(request: web.Request, assertion=None, grant_type=None, refresh_token=None, scope=None, valid_for=None) -> web.Response:
    """Generate an OAuth Token

    Returns an OAuth access token or a refresh token. You must pass a valid access token in the header of each API call.

    :param assertion: encrypted payload to identify yourself
    :type assertion: str
    :param grant_type: specify the authentication method desired
    :type grant_type: str
    :param refresh_token: The refresh token you created previously.
    :type refresh_token: str
    :param scope: set to &#x60;offline&#x60; to generate a refresh token
    :type scope: str
    :param valid_for: Number of seconds until the access token expires. Default is 60 seconds. Maximum value is 30 days
    :type valid_for: int

    """
    return web.Response(status=200)


async def revoke_refresh_token_v2(request: web.Request, token) -> web.Response:
    """Delete a Refresh Token

    

    :param token: the token to revoke
    :type token: str

    """
    return web.Response(status=200)
