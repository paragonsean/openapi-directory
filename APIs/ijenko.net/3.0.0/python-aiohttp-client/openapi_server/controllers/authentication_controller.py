from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_login import AuthLogin
from openapi_server.models.auth_refresh import AuthRefresh
from openapi_server.models.auth_reset_password import AuthResetPassword
from openapi_server.models.auth_tokens import AuthTokens
from openapi_server.models.default_error import DefaultError
from openapi_server import util


async def auth_account_login(request: web.Request, login_info) -> web.Response:
    """Get a token using login+password

    Get an access+refresh tokens pair from login and password information.  The *access token* obtained with this request can then be used in an &#x60;Access-Token&#x60; HTTP header or in a &#x60;token&#x60; URL query parameter in requests that require authentication.  The *refresh token* can be used with &#x60;/auth/refresh&#x60; when the *access token* expires to retrieve a new *access token*. The lifetime of the refresh token is the maximum lifetime of this authentication request.  The default lifetime of the *refresh token* is defined by the &#x60;appId&#x60; used. The &#x60;ttl&#x60; input parameter allows to request a *refresh token* with a shorter lifetime.  To implement *logout*, use &#x60;/auth/revoke&#x60;. 

    :param login_info: Login information.
    :type login_info: dict | bytes

    """
    login_info = AuthLogin.from_dict(login_info)
    return web.Response(status=200)


async def auth_refresh_token(request: web.Request, refresh_info) -> web.Response:
    """Refresh a token

    Get a new *access token* using a valid *refresh token*.  This is a **replacement** of the *access token*: if an existing *access token* was still not expired, it is invalidated. 

    :param refresh_info: Refresh token information.
    :type refresh_info: dict | bytes

    """
    refresh_info = AuthRefresh.from_dict(refresh_info)
    return web.Response(status=200)


async def auth_reset_password(request: web.Request, reset_password_info) -> web.Response:
    """Ask for a new password

    Trigger the request of a new password.  The account administrator will receive an e-mail with an URL pointing to a form to allow him/her to enter a new password. The old password is still functional until a new one is submitted.  Either the login or e-mail of the account must be given. 

    :param reset_password_info: Account identification information
    :type reset_password_info: dict | bytes

    """
    reset_password_info = AuthResetPassword.from_dict(reset_password_info)
    return web.Response(status=200)


async def auth_revoke_token(request: web.Request, ) -> web.Response:
    """Revoke a token

    Invalidate the authentication used for the request. The access token and the refresh token will be invalid after this request. This request is typically called to implement logout. 


    """
    return web.Response(status=200)
