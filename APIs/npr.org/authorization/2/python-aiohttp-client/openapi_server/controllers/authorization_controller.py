from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_data import AccessTokenData
from openapi_server.models.device_code_data import DeviceCodeData
from openapi_server.models.simple_error import SimpleError
from openapi_server import util


async def create_token(request: web.Request, grant_type, client_id, client_secret, code=None, redirect_uri=None, username=None, password=None, service=None, refresh_token=None, scope=None, token_type_hint=None) -> web.Response:
    """Create a new OAuth2 access token

    Please be aware that the required parameters are contingent on the &#x60;grant_type&#x60; that you select.  For the &#x60;authorization_code&#x60; grant type, you are **required** to pass in the &#x60;code&#x60; and &#x60;redirect_uri&#x60; parameters. &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  For the &#x60;client_credentials&#x60; grant type, you do not need to pass in any additional parameters beyond the basic requirements. &#x60;code&#x60;, &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  For the &#x60;device_code&#x60; grant type, you are **required** to pass in the &#x60;code&#x60; parameter. If you are a third-party developer, you are also required to provide the &#x60;scope&#x60; parameter; see the documentation for &#x60;GET /v2/authorize&#x60; for possible values. &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  For the &#x60;password&#x60; grant type, you are **required** to pass in the &#x60;username&#x60; and &#x60;password&#x60; parameters. The &#x60;code&#x60; and &#x60;redirect_uri&#x60; parameters are ignored. Third-party developers do not have access to this grant type.  For the &#x60;refresh_token&#x60; grant type, you are **required** to pass in the &#x60;refresh_token&#x60; parameter. The &#x60;scope&#x60; parameter can optionally be used to request a different set of scopes than were used in the original request, but it **cannot** contain any scopes that were not previously requested. If not specified, then &#x60;scope&#x60; will be set to whichever scopes were used for the original access token request. If trading in an old non-expiring access token for a refresh-enabled token, set the value of &#x60;refresh_token&#x60; to the access token value and &#x60;token_type_hint&#x60; must be set to &#x60;access_token&#x60;. &#x60;code&#x60;, &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  The &#x60;anonymous_user&#x60; grant type is a custom grant type created by NPR to suit our needs for functionality such as our &amp;quot;try-before-you-buy&amp;quot; experience. If you are a third-party developer, you will not have access to this grant type unless we have explicitly given you permission within our system. For this grant type, if you are a third-party developer, you are required to provide the &#x60;scope&#x60; parameter; see the documentation for &#x60;GET /v2/authorize&#x60; for possible values. &#x60;code&#x60;, &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  The &#x60;third_party&#x60; grant type is another custom grant type created by NPR to handle login via third-party providers such as Facebook and Google. If you are a third-party developer, you will not have access to this grant types unless we have explicitly given you permission within our system. For this grant type, you are **required** to pass in the &#x60;service&#x60; and &#x60;token&#x60; parameters. If you are a third-party developer, you are also required to provide the &#x60;scope&#x60; parameter; see the documentation for &#x60;GET /v2/authorize&#x60; for possible values. The &#x60;code&#x60; and &#x60;redirect_uri&#x60; parameters are ignored.  If you are unsure of which grant type to select, assume that &#x60;authorization_code&#x60; is the one you want.  Note that at this time, refresh tokens are an opt-in feature; however, in the future, they will gradually transition to being opt-out, and ultimately required for all clients. Our general guidance at this time is that if this endpoint starts returning refresh tokens for you, you are responsible for implementing the code to handle them appropriately in accordance with the OAuth 2.0 spec. For more information about our gradual rollout of this feature, please contact the NPR One API team.

    :param grant_type: The type of grant the client is requesting
    :type grant_type: str
    :param client_id: The client&#39;s ID, required for all grant types.
    :type client_id: str
    :param client_secret: The client&#39;s secret, required for all grant types.
    :type client_secret: str
    :param code: Required for &#x60;authorization_code&#x60; and &#x60;device_code&#x60; grant types. The authorization code from a successful call to &#x60;/v2/authorize&#x60;, or a device code from a successful call to &#x60;/v2/device&#x60;.
    :type code: str
    :param redirect_uri: Required for &#x60;authorization_code&#x60; grant type. The requested redirect_uri.
    :type redirect_uri: str
    :param username: Required for &#x60;password&#x60; grant type. The email address of an NPR user.
    :type username: str
    :param password: Required for &#x60;password&#x60; grant type. The password that matches the user specified with the username parameter.
    :type password: str
    :param service: Required for &#x60;third_party&#x60; grant type. The name of the third-party login provider.
    :type service: str
    :param refresh_token: Required for &#x60;refresh_token&#x60; grant type. A valid refresh token from a previous successful call to &#x60;POST /v2/token&#x60;.
    :type refresh_token: str
    :param scope: Required for third-party developers using the &#x60;device_code&#x60; and &#x60;third_party&#x60; grant types. Optionally used by the &#x60;refresh_token&#x60; grant type. A space-separated list of scope(s) requested by the application.
    :type scope: str
    :param token_type_hint: A hint about the type of the token submitted for a new access and refresh token. If unspecified, the default value is assumed to be &#x60;refresh_token&#x60;.
    :type token_type_hint: str

    """
    return web.Response(status=200)


async def generate_device_code(request: web.Request, client_id, client_secret, scope=None) -> web.Response:
    """Initiate an OAuth2 login flow for limited input devices

    This flow should only be used by clients who cannot show a native webview or do not have advanced input controls. It is an alternative to &#x60;GET /v2/authorize&#x60;.  Third-party clients will need to use one or the other of these two endpoints, but they will generally not use both.

    :param client_id: The client&#39;s ID
    :type client_id: str
    :param client_secret: The client&#39;s secret key
    :type client_secret: str
    :param scope: A space-separated list of scope(s) requested by the application. Required for all untrusted clients; will be ignored for trusted clients.
    :type scope: str

    """
    return web.Response(status=200)


async def revoke_token(request: web.Request, authorization, token, token_type_hint=None) -> web.Response:
    """Revoke an existing OAuth2 access token

    Our implementation follows the proposed IETF specification [RFC-7009](https://tools.ietf.org/html/rfc7009).  If your client application offers the ability to for a logged-in user to log out, and you have access to a long-lived &#x60;client_credentials&#x60; token (i.e. you have generated one that you are storing securely for the lifetime of the entire app install), we suggest (but do not require) that you call this endpoint and revoke the access token belonging to the logged-in user as part of your logout process. If you do not already have a long-lived &#x60;client_credentials&#x60; token, please don&#39;t generate one just for the purposes of calling this endpoint.  If you are building a prototype application, we also recommend that you use this endpoint to clean up access tokens that you generate during the testing of your app and do not intend to reuse.  Note that revoking an access token will automatically revoke any refresh tokens associated with it, and vice-versa.

    :param authorization: A &#x60;client_credentials&#x60; access token from the same client application as the token being revoked. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param token: The access token or refresh token that the client wants to have revoked.
    :type token: str
    :param token_type_hint: A hint about the type of the token submitted for revocation. If unspecified, the default value is assumed to be &#x60;access_token&#x60;.
    :type token_type_hint: str

    """
    return web.Response(status=200)
