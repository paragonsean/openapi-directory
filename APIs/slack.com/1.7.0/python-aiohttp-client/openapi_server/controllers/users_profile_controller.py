from typing import List, Dict
from aiohttp import web

from openapi_server.models.users_profile_get_error_schema import UsersProfileGetErrorSchema
from openapi_server.models.users_profile_get_schema import UsersProfileGetSchema
from openapi_server.models.users_profile_set_error_schema import UsersProfileSetErrorSchema
from openapi_server.models.users_profile_set_schema import UsersProfileSetSchema
from openapi_server import util


async def users_profile_get(request: web.Request, token, include_labels=None, user=None) -> web.Response:
    """users_profile_get

    Retrieves a user&#39;s profile information.

    :param token: Authentication token. Requires scope: &#x60;users.profile:read&#x60;
    :type token: str
    :param include_labels: Include labels for each ID in custom profile fields
    :type include_labels: bool
    :param user: User to retrieve profile info for
    :type user: str

    """
    return web.Response(status=200)


async def users_profile_set(request: web.Request, token, name=None, profile=None, user=None, value=None) -> web.Response:
    """users_profile_set

    Set the profile information for a user.

    :param token: Authentication token. Requires scope: &#x60;users.profile:write&#x60;
    :type token: str
    :param name: Name of a single key to set. Usable only if &#x60;profile&#x60; is not passed.
    :type name: str
    :param profile: Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
    :type profile: str
    :param user: ID of user to change. This argument may only be specified by team admins on paid teams.
    :type user: str
    :param value: Value to set a single key to. Usable only if &#x60;profile&#x60; is not passed.
    :type value: str

    """
    return web.Response(status=200)
