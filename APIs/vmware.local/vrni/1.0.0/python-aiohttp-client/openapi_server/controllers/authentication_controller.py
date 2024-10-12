from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.token import Token
from openapi_server.models.user_credential import UserCredential
from openapi_server import util


async def create(request: web.Request, body) -> web.Response:
    """Create an auth token

    &lt;html&gt;&lt;body&gt; vRealize Network Insight supports token based authentication.Tokens are non-modifiable identifiers returned by the system when the user has successfully authenticated using valid credentials. Token expires after expiry time returned in the response. All API requests must provide the auth token in Authorization header in following format.&lt;br&gt; Authorization &amp;#58; NetworkInsight {token} &lt;br&gt; If a token is invalid or expired, 401-Unauthorized error gets returned in the response of the API request. &lt;/body&gt;&lt;/html&gt;

    :param body: User Credentials
    :type body: dict | bytes

    """
    body = UserCredential.from_dict(body)
    return web.Response(status=200)


async def delete(request: web.Request, ) -> web.Response:
    """Delete an auth token.

    Deletes the auth token provided in Authorization header. Deleting an expired or invalid token will result in 401 Unauthorized error.


    """
    return web.Response(status=200)
