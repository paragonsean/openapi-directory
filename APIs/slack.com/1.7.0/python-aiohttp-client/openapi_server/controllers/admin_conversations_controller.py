from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_conversations_archive_error_schema import AdminConversationsArchiveErrorSchema
from openapi_server.models.admin_conversations_archive_schema import AdminConversationsArchiveSchema
from openapi_server.models.admin_conversations_convert_to_private_error_schema import AdminConversationsConvertToPrivateErrorSchema
from openapi_server.models.admin_conversations_convert_to_private_schema import AdminConversationsConvertToPrivateSchema
from openapi_server.models.admin_conversations_create_error_schema import AdminConversationsCreateErrorSchema
from openapi_server.models.admin_conversations_create_schema import AdminConversationsCreateSchema
from openapi_server.models.admin_conversations_delete_error_schema import AdminConversationsDeleteErrorSchema
from openapi_server.models.admin_conversations_delete_schema import AdminConversationsDeleteSchema
from openapi_server.models.admin_conversations_disconnect_shared_error_schema import AdminConversationsDisconnectSharedErrorSchema
from openapi_server.models.admin_conversations_get_conversation_prefs_schema import AdminConversationsGetConversationPrefsSchema
from openapi_server.models.admin_conversations_get_teams_error_schema import AdminConversationsGetTeamsErrorSchema
from openapi_server.models.admin_conversations_get_teams_schema import AdminConversationsGetTeamsSchema
from openapi_server.models.admin_conversations_invite_error_schema import AdminConversationsInviteErrorSchema
from openapi_server.models.admin_conversations_invite_schema import AdminConversationsInviteSchema
from openapi_server.models.admin_conversations_rename_schema import AdminConversationsRenameSchema
from openapi_server.models.admin_conversations_rename_schema1 import AdminConversationsRenameSchema1
from openapi_server.models.admin_conversations_search_error_schema import AdminConversationsSearchErrorSchema
from openapi_server.models.admin_conversations_search_schema import AdminConversationsSearchSchema
from openapi_server.models.admin_conversations_set_conversation_prefs_error_schema import AdminConversationsSetConversationPrefsErrorSchema
from openapi_server.models.admin_conversations_set_conversation_prefs_schema import AdminConversationsSetConversationPrefsSchema
from openapi_server.models.admin_conversations_unarchive_error_schema import AdminConversationsUnarchiveErrorSchema
from openapi_server.models.admin_conversations_unarchive_error_schema1 import AdminConversationsUnarchiveErrorSchema1
from openapi_server.models.admin_conversations_unarchive_error_schema2 import AdminConversationsUnarchiveErrorSchema2
from openapi_server.models.admin_conversations_unarchive_schema import AdminConversationsUnarchiveSchema
from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_conversations_archive(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_archive

    Archive a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to archive.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_convert_to_private(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_convert_to_private

    Convert a public channel to a private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to convert to private.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_create(request: web.Request, token, is_private, name, description=None, org_wide=None, team_id=None) -> web.Response:
    """admin_conversations_create

    Create a public or private channel-based conversation.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param is_private: When &#x60;true&#x60;, creates a private channel instead of a public channel
    :type is_private: bool
    :param name: Name of the public or private channel to create.
    :type name: str
    :param description: Description of the public or private channel to create.
    :type description: str
    :param org_wide: When &#x60;true&#x60;, the channel will be available org-wide. Note: if the channel is not &#x60;org_wide&#x3D;true&#x60;, you must specify a &#x60;team_id&#x60; for this channel
    :type org_wide: bool
    :param team_id: The workspace to create the channel in. Note: this argument is required unless you set &#x60;org_wide&#x3D;true&#x60;.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_conversations_delete(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_delete

    Delete a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to delete.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_disconnect_shared(request: web.Request, token, channel_id, leaving_team_ids=None) -> web.Response:
    """admin_conversations_disconnect_shared

    Disconnect a connected channel from one or more workspaces.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to be disconnected from some workspaces.
    :type channel_id: str
    :param leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
    :type leaving_team_ids: str

    """
    return web.Response(status=200)


async def admin_conversations_get_conversation_prefs(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_get_conversation_prefs

    Get conversation preferences for a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_id: The channel to get preferences for.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_get_teams(request: web.Request, token, channel_id, cursor=None, limit=None) -> web.Response:
    """admin_conversations_get_teams

    Get all the workspaces a given public or private channel is connected to within this Enterprise org.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_id: The channel to determine connected workspaces within the organization for.
    :type channel_id: str
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page
    :type cursor: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int

    """
    return web.Response(status=200)


async def admin_conversations_invite(request: web.Request, token, channel_id, user_ids) -> web.Response:
    """admin_conversations_invite

    Invite a user to a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel that the users will be invited to.
    :type channel_id: str
    :param user_ids: The users to invite.
    :type user_ids: str

    """
    return web.Response(status=200)


async def admin_conversations_rename(request: web.Request, token, channel_id, name) -> web.Response:
    """admin_conversations_rename

    Rename a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to rename.
    :type channel_id: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def admin_conversations_search(request: web.Request, token, team_ids=None, query=None, limit=None, cursor=None, search_channel_types=None, sort=None, sort_dir=None) -> web.Response:
    """admin_conversations_search

    Search for public or private channels in an Enterprise organization.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param team_ids: Comma separated string of team IDs, signifying the workspaces to search through.
    :type team_ids: str
    :param query: Name of the the channel to query by.
    :type query: str
    :param limit: Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str
    :param search_channel_types: The type of channel to include or exclude in the search. For example &#x60;private&#x60; will search private channels, while &#x60;private_exclude&#x60; will exclude them. For a full list of types, check the [Types section](#types).
    :type search_channel_types: str
    :param sort: Possible values are &#x60;relevant&#x60; (search ranking based on what we think is closest), &#x60;name&#x60; (alphabetical), &#x60;member_count&#x60; (number of users in the channel), and &#x60;created&#x60; (date channel was created). You can optionally pair this with the &#x60;sort_dir&#x60; arg to change how it is sorted 
    :type sort: str
    :param sort_dir: Sort direction. Possible values are &#x60;asc&#x60; for ascending order like (1, 2, 3) or (a, b, c), and &#x60;desc&#x60; for descending order like (3, 2, 1) or (c, b, a)
    :type sort_dir: str

    """
    return web.Response(status=200)


async def admin_conversations_set_conversation_prefs(request: web.Request, token, channel_id, prefs) -> web.Response:
    """admin_conversations_set_conversation_prefs

    Set the posting permissions for a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to set the prefs for
    :type channel_id: str
    :param prefs: The prefs for this channel in a stringified JSON format.
    :type prefs: str

    """
    return web.Response(status=200)


async def admin_conversations_set_teams(request: web.Request, token, channel_id, org_channel=None, target_team_ids=None, team_id=None) -> web.Response:
    """admin_conversations_set_teams

    Set the workspaces in an Enterprise grid org that connect to a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The encoded &#x60;channel_id&#x60; to add or remove to workspaces.
    :type channel_id: str
    :param org_channel: True if channel has to be converted to an org channel
    :type org_channel: bool
    :param target_team_ids: A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.
    :type target_team_ids: str
    :param team_id: The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_conversations_unarchive(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_unarchive

    Unarchive a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to unarchive.
    :type channel_id: str

    """
    return web.Response(status=200)
