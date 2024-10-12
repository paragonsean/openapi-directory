from typing import List, Dict
from aiohttp import web

from openapi_server.models.exchange_refresh_token_for_access_token_request import ExchangeRefreshTokenForAccessTokenRequest
from openapi_server.models.revoke_an_access_token_request import RevokeAnAccessTokenRequest
from openapi_server import util


async def authorize_application(request: web.Request, response_type, client_id, redirect_uri, state=None, body=None) -> web.Response:
    """Authorize Application

    Construct then redirect to this URL. The Trakt website will request permissions for your app, which the user needs to approve. If the user isn&#39;t signed into Trakt, it will ask them to do so. Send &#x60;signup&#x3D;true&#x60; if you prefer the account sign up page to be the default.  **Note:** You should use the normal **https://trakt.tv** hostname when creating this URL and not the API URL.

    :param response_type: Must be set to code.
    :type response_type: str
    :param client_id: Get this from your app settings.
    :type client_id: str
    :param redirect_uri: URI specified in your app settings.
    :type redirect_uri: str
    :param state: State variable for CSRF purposes.
    :type state: str
    :param body: Default to the sign up page.
    :type body: str

    """
    return web.Response(status=200)


async def exchange_refresh_token_for_access_token(request: web.Request, body=None) -> web.Response:
    """Exchange refresh_token for access_token

    Use the &#x60;refresh_token&#x60; to get a new &#x60;access_token&#x60; without asking the user to re-authenticate. The &#x60;access_token&#x60; is valid for 3 months before it needs to be refreshed again.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;refresh_token&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Saved from the initial token method. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;redirect_uri&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | URI specified in your app settings. | | &#x60;grant_type&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;* &lt;/a&gt; | string | &#x60;refresh_token&#x60; |

    :param body: 
    :type body: dict | bytes

    """
    body = ExchangeRefreshTokenForAccessTokenRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_an_access_token(request: web.Request, body=None) -> web.Response:
    """Revoke an access_token

    An &#x60;access_token&#x60; can be revoked when a user signs out of their Trakt account in your app. This is not required, but might improve the user experience so the user doesn&#39;t have an unused app connection hanging around.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;token&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | A valid OAuth &#x60;access_token&#x60;. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |

    :param body: 
    :type body: dict | bytes

    """
    body = RevokeAnAccessTokenRequest.from_dict(body)
    return web.Response(status=200)
