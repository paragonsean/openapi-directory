from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.login_request import LoginRequest
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.radius_challenge_response import RadiusChallengeResponse
from openapi_server.models.recover_user_name_request import RecoverUserNameRequest
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.reset_password_request import ResetPasswordRequest
from openapi_server.models.reset_password_token_validate_response import ResetPasswordTokenValidateResponse
from openapi_server.models.reset_password_with_token_request import ResetPasswordWithTokenRequest
from openapi_server import util


async def complete_open_id_login(request: web.Request, code, state, id_token=None) -> web.Response:
    """Complete OpenID Connect authentication

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.14.0&lt;/h3&gt;  ### Description:   This is the second step of the OpenID Connect authentication.   The user hands over the authorization code and is logged in.  ### Precondition: Existing user with activated OpenID Connect authentication that is **NOT** locked.  ### Postcondition: User is logged in.  ### Further Information: None.

    :param code: Authorization code
    :type code: str
    :param state: Authentication state
    :type state: str
    :param id_token: Identity token
    :type id_token: str

    """
    return web.Response(status=200)


async def initiate_open_id_login(request: web.Request, issuer, redirect_uri, language, test) -> web.Response:
    """Initiate OpenID Connect authentication

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.14.0&lt;/h3&gt;  ### Description: This is the first step of the OpenID Connect authentication.   The user is send to the OpenID Connect identity provider to authenticate himself and retrieve an authorization code.  ### Precondition: None.  ### Postcondition: User is redirected to OpenID Connect identity provider to authenticate himself.  ### Further Information: None.

    :param issuer: Issuer identifier of the OpenID Connect identity provider
    :type issuer: str
    :param redirect_uri: Redirect URI to complete the OpenID Connect authentication
    :type redirect_uri: str
    :param language: Language ID or ISO 639-1 code
    :type language: str
    :param test: Flag to test the authentication parameters.  If the request is valid, the API will respond with &#x60;204 No Content&#x60;.
    :type test: bool

    """
    return web.Response(status=200)


async def login(request: web.Request, body) -> web.Response:
    """Authenticate user (Login)

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.13.0&lt;/h3&gt;  ### Description: Authenticates user and provides an authentication token (&#x60;X-Sds-Auth-Token&#x60;) that is required for the most operations.  ### Precondition: Existing user that is **NOT** locked.  ### Postcondition: User is logged in.  ### Further Information: The provided token is valid for **two hours**, every usage resets this period to two full hours again.   Logging off invalidates the token.    ### Available authentication methods: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method (&#x60;authType&#x60;) | Description | | :--- | :--- | | &#x60;basic&#x60; | Log in with credentials stored in the database &lt;br&gt;Formerly known as &#x60;sql&#x60;.| | &#x60;active_directory&#x60; | Log in with Active Directory credentials | | &#x60;radius&#x60; | Log in with RADIUS username, PIN and token password.&lt;br&gt;Token (request parameter) may be set, otherwise this parameter is ignored. If token is set, password is optional. | | &#x60;openid&#x60; | Please use &#x60;POST /auth/openid/login&#x60; API to login with OpenID Connect identity |  &lt;/details&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = LoginRequest.from_dict(body)
    return web.Response(status=200)


async def ping(request: web.Request, ) -> web.Response:
    """Ping

    ### Description: Test connection to DRACOON Core Service.  ### Precondition: None.  ### Postcondition: &#x60;200 OK&#x60; with current date string is returned if successful.  ### Further Information: None.


    """
    return web.Response(status=200)


async def recover_user_name(request: web.Request, body) -> web.Response:
    """Recover username

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.13.0&lt;/h3&gt;  ### Description:   Request an email with the user names of all accounts connected to the email.  ### Precondition: Valid email address.  ### Postcondition: An email is sent to the provided address, with a list of account user names connected to it.  ### Further Information: None. 

    :param body: 
    :type body: dict | bytes

    """
    body = RecoverUserNameRequest.from_dict(body)
    return web.Response(status=200)


async def request_password_reset(request: web.Request, body) -> web.Response:
    """Request password reset

    ### Description:   Request an email with a password reset token for a certain user to reset password.  ### Precondition: Registered user account.  ### Postcondition: Provided user receives email with password reset token.  ### Further Information: None.

    :param body: 
    :type body: dict | bytes

    """
    body = ResetPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def reset_password(request: web.Request, token, body) -> web.Response:
    """Reset password

    ### Description:   Resets user&#39;s password.  ### Precondition: User received a password reset token.  ### Postcondition: User&#39;s password is reset to the provided password.  ### Further Information: Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]

    :param token: Password reset token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResetPasswordWithTokenRequest.from_dict(body)
    return web.Response(status=200)


async def validate_reset_password_token(request: web.Request, token) -> web.Response:
    """Validate information for password reset

    ### Description:   Request all information for a password change dialogue e.g. real name of user.  ### Precondition: User received a password reset token.  ### Postcondition: Context information is returned.  ### Further Information: None.

    :param token: Password reset token
    :type token: str

    """
    return web.Response(status=200)
