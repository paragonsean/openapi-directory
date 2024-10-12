from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_users_assign(request: web.Request, token, team_id, user_id, channel_ids=None, is_restricted=None, is_ultra_restricted=None) -> web.Response:
    """admin_users_assign

    Add an Enterprise user to a workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to add to the workspace.
    :type user_id: str
    :param channel_ids: Comma separated values of channel IDs to add user in the new workspace.
    :type channel_ids: str
    :param is_restricted: True if user should be added to the workspace as a guest.
    :type is_restricted: bool
    :param is_ultra_restricted: True if user should be added to the workspace as a single-channel guest.
    :type is_ultra_restricted: bool

    """
    return web.Response(status=200)


async def admin_users_invite(request: web.Request, token, channel_ids, email, team_id, custom_message=None, guest_expiration_ts=None, is_restricted=None, is_ultra_restricted=None, real_name=None, resend=None) -> web.Response:
    """admin_users_invite

    Invite a user to a workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param channel_ids: A comma-separated list of &#x60;channel_id&#x60;s for this user to join. At least one channel is required.
    :type channel_ids: str
    :param email: The email address of the person to invite.
    :type email: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param custom_message: An optional message to send to the user in the invite email.
    :type custom_message: str
    :param guest_expiration_ts: Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.
    :type guest_expiration_ts: str
    :param is_restricted: Is this user a multi-channel guest user? (default: false)
    :type is_restricted: bool
    :param is_ultra_restricted: Is this user a single channel guest user? (default: false)
    :type is_ultra_restricted: bool
    :param real_name: Full name of the user.
    :type real_name: str
    :param resend: Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
    :type resend: bool

    """
    return web.Response(status=200)


async def admin_users_list(request: web.Request, token, team_id, cursor=None, limit=None) -> web.Response:
    """admin_users_list

    List users on a workspace

    :param token: Authentication token. Requires scope: &#x60;admin.users:read&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str
    :param limit: Limit for how many users to be retrieved per page
    :type limit: int

    """
    return web.Response(status=200)


async def admin_users_remove(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_remove

    Remove a user from a workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to remove.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_set_admin(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_set_admin

    Set an existing guest, regular user, or owner to be an admin user.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to designate as an admin.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_set_expiration(request: web.Request, token, expiration_ts, team_id, user_id) -> web.Response:
    """admin_users_set_expiration

    Set an expiration for a guest user

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param expiration_ts: Timestamp when guest account should be disabled.
    :type expiration_ts: int
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to set an expiration for.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_set_owner(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_set_owner

    Set an existing guest, regular user, or admin user to be a workspace owner.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: Id of the user to promote to owner.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_set_regular(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_set_regular

    Set an existing guest user, admin user, or owner to be a regular user.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to designate as a regular user.
    :type user_id: str

    """
    return web.Response(status=200)
