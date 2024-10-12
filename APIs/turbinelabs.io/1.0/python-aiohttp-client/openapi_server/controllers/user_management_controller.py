from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.access_token_description import AccessTokenDescription
from openapi_server.models.error import Error
from openapi_server.models.multi_access_tokens import MultiAccessTokens
from openapi_server.models.user import User
from openapi_server import util


async def admin_user_self_access_token_access_token_key_delete(request: web.Request, access_token_key, checksum) -> web.Response:
    """Delete the specified access token.

    

    :param access_token_key: the key of the Access Token that should be deleted
    :type access_token_key: str
    :param checksum: the current checksum of the user to be modified
    :type checksum: str

    """
    return web.Response(status=200)


async def admin_user_self_access_tokens_get(request: web.Request, ) -> web.Response:
    """Lists Access Tokens that are configured for the authenticated user.

    


    """
    return web.Response(status=200)


async def admin_user_self_access_tokens_post(request: web.Request, description) -> web.Response:
    """Creates a new Access Token and associates it with the authenticated user.

    

    :param description: A short string (&lt;255 characters) describing the expected use of the token.
    :type description: dict | bytes

    """
    description = AccessTokenDescription.from_dict(description)
    return web.Response(status=200)


async def admin_user_self_get(request: web.Request, ) -> web.Response:
    """Returns the user object for the account authorized and making this request.

    Request the user object for an authorized requesting account.


    """
    return web.Response(status=200)
