from typing import List, Dict
from aiohttp import web

from openapi_server.models.oauth_v1_token import OauthV1Token
from openapi_server import util


async def create_token(request: web.Request, client_sid, grant_type, client_secret=None, code=None, code_verifier=None, device_code=None, device_id=None, refresh_token=None) -> web.Response:
    """create_token

    Issues a new Access token (optionally identity_token &amp; refresh_token) in exchange of Oauth grant

    :param client_sid: A 34 character string that uniquely identifies this OAuth App.
    :type client_sid: str
    :param grant_type: Grant type is a credential representing resource owner&#39;s authorization which can be used by client to obtain access token.
    :type grant_type: str
    :param client_secret: The credential for confidential OAuth App.
    :type client_secret: str
    :param code: JWT token related to the authorization code grant type.
    :type code: str
    :param code_verifier: A code which is generation cryptographically.
    :type code_verifier: str
    :param device_code: JWT token related to the device code grant type.
    :type device_code: str
    :param device_id: The Id of the device associated with the token (refresh token).
    :type device_id: str
    :param refresh_token: JWT token related to the refresh token grant type.
    :type refresh_token: str

    """
    return web.Response(status=200)
