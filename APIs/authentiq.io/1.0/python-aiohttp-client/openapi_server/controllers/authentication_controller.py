from typing import List, Dict
from aiohttp import web

from openapi_server.models.o_auth2_error import OAuth2Error
from openapi_server.models.token import Token
from openapi_server.models.user_info import UserInfo
from openapi_server import util


async def authorize(request: web.Request, client_id, response_type, scope, redirect_uri, state, response_mode=None, nonce=None, display=None, prompt=None, max_age=None, ui_locales=None) -> web.Response:
    """Authenticate a user

    Start a session with Authentiq Connect to authenticate a user.  &#x60;&#x60;&#x60; GET https://connect.authentiq.io/authorize?client_id&#x3D;&lt;your-client-id&gt;&amp;response_type&#x3D;code+id_token&amp;scope&#x3D;openid+email&amp;redirect_uri&#x3D;&lt;your-redirect-uri&gt;&amp;state&#x3D;0123456789 &#x60;&#x60;&#x60;  This endpoint also supports the POST method. 

    :param client_id: A client ID obtained from the [Dashboard](https://dashboard.authentiq.com/). 
    :type client_id: str
    :param response_type: The OIDC response type to use for this authentication flow. Valid choices are &#x60;code&#x60;, &#x60;id_token&#x60;, &#x60;token&#x60;, &#x60;token id_token&#x60;, &#x60;code id_token&#x60; &#x60;code token&#x60; and &#x60;code token id_token&#x60;, but a client can be configured with a more restricted set. 
    :type response_type: str
    :param scope: The space-separated identity claims to request from the end-user. Always include &#x60;openid&#x60; as a scope for compatibility with OIDC. 
    :type scope: str
    :param redirect_uri: The location to redirect to after (un)successful authentication. See OIDC for the parameters passed in the query string (&#x60;response_mode&#x3D;query&#x60;) or as fragments (&#x60;response_mode&#x3D;fragment&#x60;). Unless the client is in test-mode this must be one of the registered redirect URLs. 
    :type redirect_uri: str
    :param state: An opaque string that will be passed back to the redirect URL and therefore can be used to communicate client side state and prevent CSRF attacks. 
    :type state: str
    :param response_mode: Whether to append parameters to the redirect URL in the query string (&#x60;query&#x60;) or as fragments (&#x60;fragment&#x60;). This option usually has a sensible default for each of the response types. 
    :type response_mode: str
    :param nonce: An nonce provided by the client (and opaque to Authentiq Connect) that will be included in any ID Token generated for this session. Clients should use the nonce to mitigate replay attacks. 
    :type nonce: str
    :param display: The authentication display mode, which can be one of &#x60;page&#x60;, &#x60;popup&#x60; or &#x60;modal&#x60;. Defaults to &#x60;page&#x60;. 
    :type display: str
    :param prompt: Space-delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for reauthentication and consent. The supported values are: &#x60;none&#x60;, &#x60;login&#x60;, &#x60;consent&#x60;. If &#x60;consent&#x60; the end-user is asked to (re)confirm what claims they share. Use &#x60;none&#x60; to check for an active session. 
    :type prompt: str
    :param max_age: Specifies the allowable elapsed time in seconds since the last time the end-user was actively authenticated. 
    :type max_age: int
    :param ui_locales: Specifies the preferred language to use on the authorization page, as a space-separated list of BCP47 language tags. Ignored at the moment. 
    :type ui_locales: str

    """
    return web.Response(status=200)


async def token(request: web.Request, client_id, client_secret, code, grant_type, redirect_uri, authorization=None) -> web.Response:
    """Obtain an ID Token

    Exchange en authorization code for an ID Token or Access Token.  This endpoint supports both &#x60;client_secret_basic&#x60; (default) and &#x60;client_secret_basic&#x60; authentication methods, as specified by the client&#39;s &#x60;token_endpoint_auth_method&#x60;. 

    :param client_id: The registered client ID. 
    :type client_id: str
    :param client_secret: The registered client ID secret. 
    :type client_secret: str
    :param code: The authorization code previously obtained from the Authentication endpoint. 
    :type code: str
    :param grant_type: The authorization grant type, must be &#x60;authorization_code&#x60;. 
    :type grant_type: str
    :param redirect_uri: The redirect URL that was used previously with the Authentication endpoint. 
    :type redirect_uri: str
    :param authorization: HTTP Basic authorization header. 
    :type authorization: str

    """
    return web.Response(status=200)


async def user_info(request: web.Request, ) -> web.Response:
    """Retrieve a user profile

    Use this endpoint to retrieve a user&#39;s profile in case you are unable to parse an ID Token or you&#39;ve not already obtained enough details from the ID Token via the Token Endpoint. 


    """
    return web.Response(status=200)
