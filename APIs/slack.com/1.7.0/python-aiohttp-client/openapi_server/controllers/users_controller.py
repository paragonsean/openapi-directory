from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_method_users_get_presence import APIMethodUsersGetPresence
from openapi_server.models.users_conversations_error_schema import UsersConversationsErrorSchema
from openapi_server.models.users_conversations_success_schema import UsersConversationsSuccessSchema
from openapi_server.models.users_counts_error_schema import UsersCountsErrorSchema
from openapi_server.models.users_delete_photo_error_schema import UsersDeletePhotoErrorSchema
from openapi_server.models.users_delete_photo_schema import UsersDeletePhotoSchema
from openapi_server.models.users_identity_error_schema import UsersIdentityErrorSchema
from openapi_server.models.users_identity_schema_inner import UsersIdentitySchemaInner
from openapi_server.models.users_info_error_schema import UsersInfoErrorSchema
from openapi_server.models.users_info_success_schema import UsersInfoSuccessSchema
from openapi_server.models.users_list_error_schema import UsersListErrorSchema
from openapi_server.models.users_list_schema import UsersListSchema
from openapi_server.models.users_lookup_by_email_error_schema import UsersLookupByEmailErrorSchema
from openapi_server.models.users_lookup_by_email_success_schema import UsersLookupByEmailSuccessSchema
from openapi_server.models.users_profile_get_error_schema import UsersProfileGetErrorSchema
from openapi_server.models.users_profile_get_schema import UsersProfileGetSchema
from openapi_server.models.users_profile_set_error_schema import UsersProfileSetErrorSchema
from openapi_server.models.users_profile_set_schema import UsersProfileSetSchema
from openapi_server.models.users_set_active_error_schema import UsersSetActiveErrorSchema
from openapi_server.models.users_set_active_schema import UsersSetActiveSchema
from openapi_server.models.users_set_photo_error_schema import UsersSetPhotoErrorSchema
from openapi_server.models.users_set_photo_schema import UsersSetPhotoSchema
from openapi_server.models.users_set_presence_error_schema import UsersSetPresenceErrorSchema
from openapi_server.models.users_set_presence_schema import UsersSetPresenceSchema
from openapi_server import util


async def users_conversations(request: web.Request, token=None, user=None, types=None, exclude_archived=None, limit=None, cursor=None) -> web.Response:
    """users_conversations

    List conversations the calling user may access.

    :param token: Authentication token. Requires scope: &#x60;conversations:read&#x60;
    :type token: str
    :param user: Browse conversations by a specific user ID&#39;s membership. Non-public channels are restricted to those where the calling user shares membership.
    :type user: str
    :param types: Mix and match channel types by providing a comma-separated list of any combination of &#x60;public_channel&#x60;, &#x60;private_channel&#x60;, &#x60;mpim&#x60;, &#x60;im&#x60;
    :type types: str
    :param exclude_archived: Set to &#x60;true&#x60; to exclude archived channels from the list
    :type exclude_archived: bool
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. Must be an integer no larger than 1000.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str

    """
    return web.Response(status=200)


async def users_delete_photo(request: web.Request, token) -> web.Response:
    """users_delete_photo

    Delete the user profile photo

    :param token: Authentication token. Requires scope: &#x60;users.profile:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def users_get_presence(request: web.Request, token, user=None) -> web.Response:
    """users_get_presence

    Gets user presence information.

    :param token: Authentication token. Requires scope: &#x60;users:read&#x60;
    :type token: str
    :param user: User to get presence info on. Defaults to the authed user.
    :type user: str

    """
    return web.Response(status=200)


async def users_identity(request: web.Request, token=None) -> web.Response:
    """users_identity

    Get a user&#39;s identity.

    :param token: Authentication token. Requires scope: &#x60;identity.basic&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def users_info(request: web.Request, token, include_locale=None, user=None) -> web.Response:
    """users_info

    Gets information about a user.

    :param token: Authentication token. Requires scope: &#x60;users:read&#x60;
    :type token: str
    :param include_locale: Set this to &#x60;true&#x60; to receive the locale for this user. Defaults to &#x60;false&#x60;
    :type include_locale: bool
    :param user: User to get info on
    :type user: str

    """
    return web.Response(status=200)


async def users_list(request: web.Request, token=None, limit=None, cursor=None, include_locale=None) -> web.Response:
    """users_list

    Lists all users in a Slack team.

    :param token: Authentication token. Requires scope: &#x60;users:read&#x60;
    :type token: str
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. Providing no &#x60;limit&#x60; value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience &#x60;limit_required&#x60; or HTTP 500 errors.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str
    :param include_locale: Set this to &#x60;true&#x60; to receive the locale for users. Defaults to &#x60;false&#x60;
    :type include_locale: bool

    """
    return web.Response(status=200)


async def users_lookup_by_email(request: web.Request, token, email) -> web.Response:
    """users_lookup_by_email

    Find a user with an email address.

    :param token: Authentication token. Requires scope: &#x60;users:read.email&#x60;
    :type token: str
    :param email: An email address belonging to a user in the workspace
    :type email: str

    """
    return web.Response(status=200)


async def users_profile_get_0(request: web.Request, token, include_labels=None, user=None) -> web.Response:
    """users_profile_get_0

    Retrieves a user&#39;s profile information.

    :param token: Authentication token. Requires scope: &#x60;users.profile:read&#x60;
    :type token: str
    :param include_labels: Include labels for each ID in custom profile fields
    :type include_labels: bool
    :param user: User to retrieve profile info for
    :type user: str

    """
    return web.Response(status=200)


async def users_profile_set_0(request: web.Request, token, name=None, profile=None, user=None, value=None) -> web.Response:
    """users_profile_set_0

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


async def users_set_active(request: web.Request, token) -> web.Response:
    """users_set_active

    Marked a user as active. Deprecated and non-functional.

    :param token: Authentication token. Requires scope: &#x60;users:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def users_set_photo(request: web.Request, token, crop_w=None, crop_x=None, crop_y=None, image=None) -> web.Response:
    """users_set_photo

    Set the user profile photo

    :param token: Authentication token. Requires scope: &#x60;users.profile:write&#x60;
    :type token: str
    :param crop_w: Width/height of crop box (always square)
    :type crop_w: str
    :param crop_x: X coordinate of top-left corner of crop box
    :type crop_x: str
    :param crop_y: Y coordinate of top-left corner of crop box
    :type crop_y: str
    :param image: File contents via &#x60;multipart/form-data&#x60;.
    :type image: str

    """
    return web.Response(status=200)


async def users_set_presence(request: web.Request, token, presence) -> web.Response:
    """users_set_presence

    Manually sets user presence.

    :param token: Authentication token. Requires scope: &#x60;users:write&#x60;
    :type token: str
    :param presence: Either &#x60;auto&#x60; or &#x60;away&#x60;
    :type presence: str

    """
    return web.Response(status=200)
