from typing import List, Dict
from aiohttp import web

from openapi_server.models.oauth_access_token_post200_response import OauthAccessTokenPost200Response
from openapi_server.models.oauth_access_token_post_request import OauthAccessTokenPostRequest
from openapi_server.models.oauth_live_session_token_post200_response import OauthLiveSessionTokenPost200Response
from openapi_server.models.oauth_live_session_token_post_request import OauthLiveSessionTokenPostRequest
from openapi_server.models.oauth_request_token_post200_response import OauthRequestTokenPost200Response
from openapi_server.models.oauth_request_token_post_request import OauthRequestTokenPostRequest
from openapi_server import util


async def oauth_access_token_post(request: web.Request, body) -> web.Response:
    """Obtain a access token

    Obtain an access token using the request token and the verification code you received after the user provided authorization. See section 6.3 of the OAuth v1.0a specification for more details.  

    :param body: OAuth Parameters
    :type body: dict | bytes

    """
    body = OauthAccessTokenPostRequest.from_dict(body)
    return web.Response(status=200)


async def oauth_live_session_token_post(request: web.Request, body) -> web.Response:
    """Obtain a live session token

    In order to access protected IB resources, a live session token is required. This endpoint allows consumers to obtain a live session token to access these resources using an OAuth access token and the Diffie-Hellman prime and generator supplied during the registration process. Note this is an additional IB-specific step, and not part of the OAuth v1.0a specification. Please refer to the \&quot;OAuth at Interactive Brokers\&quot; document for more details.  https://www.interactivebrokers.com/webtradingapi/oauth.pdf 

    :param body: OAuth Parameters
    :type body: dict | bytes

    """
    body = OauthLiveSessionTokenPostRequest.from_dict(body)
    return web.Response(status=200)


async def oauth_request_token_post(request: web.Request, body) -> web.Response:
    """Obtain a request token

    Obtain a request token. See section 6.1 of the OAuth v1.0a specification for more information. http://oauth.net/core/1.0a/#auth_step1  Note we do not return an oauth_token_secret in the response as we are using RSA signatures rather than PLAINTEXT authentication.  

    :param body: OAuth Parameters
    :type body: dict | bytes

    """
    body = OauthRequestTokenPostRequest.from_dict(body)
    return web.Response(status=200)
