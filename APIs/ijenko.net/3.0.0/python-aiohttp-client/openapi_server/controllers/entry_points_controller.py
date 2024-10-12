from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_login import AuthLogin
from openapi_server.models.auth_tokens import AuthTokens
from openapi_server.models.default_error import DefaultError
from openapi_server.models.place_item import PlaceItem
from openapi_server.models.user_me import UserMe
from openapi_server.models.user_me_patch import UserMePatch
from openapi_server import util


async def auth_account_login_0(request: web.Request, login_info) -> web.Response:
    """Get a token using login+password

    Get an access+refresh tokens pair from login and password information.  The *access token* obtained with this request can then be used in an &#x60;Access-Token&#x60; HTTP header or in a &#x60;token&#x60; URL query parameter in requests that require authentication.  The *refresh token* can be used with &#x60;/auth/refresh&#x60; when the *access token* expires to retrieve a new *access token*. The lifetime of the refresh token is the maximum lifetime of this authentication request.  The default lifetime of the *refresh token* is defined by the &#x60;appId&#x60; used. The &#x60;ttl&#x60; input parameter allows to request a *refresh token* with a shorter lifetime.  To implement *logout*, use &#x60;/auth/revoke&#x60;. 

    :param login_info: Login information.
    :type login_info: dict | bytes

    """
    login_info = AuthLogin.from_dict(login_info)
    return web.Response(status=200)


async def me_get(request: web.Request, ) -> web.Response:
    """Information about the User

    Get information on the authenticated *User* who does the request.  The *login* property is returned only if the *User* is the administrator of the *Account*. 


    """
    return web.Response(status=200)


async def me_patch(request: web.Request, user_patch) -> web.Response:
    """Update User information

    Update *User* information (locale). 

    :param user_patch: Updated user info.
    :type user_patch: dict | bytes

    """
    user_patch = UserMePatch.from_dict(user_patch)
    return web.Response(status=200)


async def me_places(request: web.Request, embed_metadata=None) -> web.Response:
    """List accessible Places

    List the *Places* to which the *Token* has access.

    :param embed_metadata: Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    :type embed_metadata: List[str]

    """
    return web.Response(status=200)
