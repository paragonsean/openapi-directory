from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_users2_fa_login_error_response import PostUsers2FALoginErrorResponse
from openapi_server.models.post_users_login_error_response import PostUsersLoginErrorResponse
from openapi_server.models.post_users_login_success_response import PostUsersLoginSuccessResponse
from openapi_server.models.users2_fa_login_request import Users2FALoginRequest
from openapi_server.models.users_login_request import UsersLoginRequest
from openapi_server import util


async def post_users2_fa_login(request: web.Request, body) -> web.Response:
    """Second factor authentication.

    When a user has 2FA enabled, this is the second call to perform after &#x60;/v2/users/login&#x60; call.  Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.  The returned token is used in the HTTP Authorization header like &#x60;Authorization: Bearer {TOKEN}&#x60;.  Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository. 

    :param body: Login details.
    :type body: dict | bytes

    """
    body = Users2FALoginRequest.from_dict(body)
    return web.Response(status=200)


async def post_users_login(request: web.Request, body) -> web.Response:
    """Create an authentication token

    Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.  The returned token is used in the HTTP Authorization header like &#x60;Authorization: Bearer {TOKEN}&#x60;.  Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository. 

    :param body: Login details.
    :type body: dict | bytes

    """
    body = UsersLoginRequest.from_dict(body)
    return web.Response(status=200)
