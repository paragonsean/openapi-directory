from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server.models.user_collection import UserCollection
from openapi_server.models.user_definition import UserDefinition
from openapi_server import util


async def create_users(request: web.Request, authorization, body) -> web.Response:
    """Create User

    Creates a new organization user and adds them to the user domain. The user email domain must match an existing organization email domain.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param body: The details of the user to create
    :type body: dict | bytes

    """
    body = UserDefinition.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, authorization, user_key) -> web.Response:
    """Delete User

    Deletes a user from the organization (but not from the account).

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param user_key: The key of the user to query. The user must be in the organization domain
    :type user_key: int

    """
    return web.Response(status=200)


async def get_me(request: web.Request, authorization) -> web.Response:
    """Get Current User

    Queries the identity of the current authenticated user.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, authorization, user_key) -> web.Response:
    """Get User

    Queries user identity in the organization domain.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param user_key: The key of the user to query. The user must be in the organization domain
    :type user_key: int

    """
    return web.Response(status=200)


async def get_users(request: web.Request, authorization, filter=None) -> web.Response:
    """Get Users

    Queries multiple user identities in the organization domain. Filtering is available.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param filter:  Without a filter, all users in a user domain are returned. The filter parameter must be a properly formed SCIM filter using either the operator eq (equals) or the operator sw (starts with). The filter works for userName, displayName, name.givenName, and name.familyName attributes. For example, /Users?filter&#x3D;name.familyName%20eq%20%%22Smith%22
    :type filter: str

    """
    return web.Response(status=200)


async def replace_me(request: web.Request, authorization, body) -> web.Response:
    """Replace Current User

    Changes the current authenticated user&#39;s displayName, locale, timezone, username and password. The request must include the full user definition (to modify one or more values without sending the full definition, see Update User). The replaced user email domain must be an existing organization email domain. 

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param body: The new user data
    :type body: dict | bytes

    """
    body = UserDefinition.from_dict(body)
    return web.Response(status=200)


async def replace_user(request: web.Request, authorization, user_key, body) -> web.Response:
    """Replace User

    Changes an existing user&#39;s displayName, locale, timezone, username and password. The request must include the full user definition (to modify one or more values without sending the full definition, see Update User). The replaced user email domain must be an existing organization email domain.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param user_key: The key of the user to query. The user must be in the organization domain
    :type user_key: int
    :param body: The new user data
    :type body: dict | bytes

    """
    body = UserDefinition.from_dict(body)
    return web.Response(status=200)


async def update_me(request: web.Request, authorization, body) -> web.Response:
    """Update Current User

    Changes a limited set (or all if you choose) of the current authenticated user&#39;s data. The updated user email domain must be an existing organization email domain. 

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param body: The new user data
    :type body: dict | bytes

    """
    body = UserDefinition.from_dict(body)
    return web.Response(status=200)


async def update_user(request: web.Request, authorization, user_key, body) -> web.Response:
    """Update User

    Changes a limited set (or all if you choose) of the user&#39;s data. The updated user email domain must be an existing organization email domain.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param user_key: The key of the user to query. The user must be in the organization domain
    :type user_key: int
    :param body: The new user data
    :type body: dict | bytes

    """
    body = UserDefinition.from_dict(body)
    return web.Response(status=200)
