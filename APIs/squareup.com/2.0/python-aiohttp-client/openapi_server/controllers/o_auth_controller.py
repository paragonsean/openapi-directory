from typing import List, Dict
from aiohttp import web

from openapi_server.models.obtain_token_request import ObtainTokenRequest
from openapi_server.models.obtain_token_response import ObtainTokenResponse
from openapi_server.models.renew_token_request import RenewTokenRequest
from openapi_server.models.renew_token_response import RenewTokenResponse
from openapi_server.models.revoke_token_request import RevokeTokenRequest
from openapi_server.models.revoke_token_response import RevokeTokenResponse
from openapi_server import util


async def obtain_token(request: web.Request, body) -> web.Response:
    """ObtainToken

    Returns an OAuth access token.  The endpoint supports distinct methods of obtaining OAuth access tokens. Applications specify a method by adding the &#x60;grant_type&#x60; parameter in the request and also provide relevant information.  __Note:__ Regardless of the method application specified, the endpoint always returns two items; an OAuth access token and a refresh token in the response.  __OAuth tokens should only live on secure servers. Application clients should never interact directly with OAuth tokens__.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = ObtainTokenRequest.from_dict(body)
    return web.Response(status=200)


async def renew_token(request: web.Request, client_id, body) -> web.Response:
    """RenewToken

    &#x60;RenewToken&#x60; is deprecated. For information about refreshing OAuth access tokens, see [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).   Renews an OAuth access token before it expires.  OAuth access tokens besides your application&#39;s personal access token expire after __30 days__. You can also renew expired tokens within __15 days__ of their expiration. You cannot renew an access token that has been expired for more than 15 days. Instead, the associated user must re-complete the OAuth flow from the beginning.  __Important:__ The &#x60;Authorization&#x60; header for this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Client APPLICATION_SECRET &#x60;&#x60;&#x60;  Replace &#x60;APPLICATION_SECRET&#x60; with the application secret on the Credentials page in the [developer dashboard](https://developer.squareup.com/apps).

    :param client_id: Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).
    :type client_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RenewTokenRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_token(request: web.Request, body) -> web.Response:
    """RevokeToken

    Revokes an access token generated with the OAuth flow.  If an account has more than one OAuth access token for your application, this endpoint revokes all of them, regardless of which token you specify. When an OAuth access token is revoked, all of the active subscriptions associated with that OAuth token are canceled immediately.  __Important:__ The &#x60;Authorization&#x60; header for this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Client APPLICATION_SECRET &#x60;&#x60;&#x60;  Replace &#x60;APPLICATION_SECRET&#x60; with the application secret on the OAuth page in the [developer dashboard](https://developer.squareup.com/apps).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RevokeTokenRequest.from_dict(body)
    return web.Response(status=200)
