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


async def admin_apps_approve_0(request: web.Request, token, app_id=None, request_id=None, team_id=None) -> web.Response:
    """admin_apps_approve_0

    Approve an app for installation on a workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.apps:write&#x60;
    :type token: str
    :param app_id: The id of the app to approve.
    :type app_id: str
    :param request_id: The id of the request to approve.
    :type request_id: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_apps_approved_list_0(request: web.Request, token, limit=None, cursor=None, team_id=None, enterprise_id=None) -> web.Response:
    """admin_apps_approved_list_0

    List approved apps for an org or workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.apps:read&#x60;
    :type token: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page
    :type cursor: str
    :param team_id: 
    :type team_id: str
    :param enterprise_id: 
    :type enterprise_id: str

    """
    return web.Response(status=200)


async def admin_apps_requests_list_0(request: web.Request, token, limit=None, cursor=None, team_id=None) -> web.Response:
    """admin_apps_requests_list_0

    List app requests for a team/workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.apps:read&#x60;
    :type token: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page
    :type cursor: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_apps_restrict_0(request: web.Request, token, app_id=None, request_id=None, team_id=None) -> web.Response:
    """admin_apps_restrict_0

    Restrict an app for installation on a workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.apps:write&#x60;
    :type token: str
    :param app_id: The id of the app to restrict.
    :type app_id: str
    :param request_id: The id of the request to restrict.
    :type request_id: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_apps_restricted_list_0(request: web.Request, token, limit=None, cursor=None, team_id=None, enterprise_id=None) -> web.Response:
    """admin_apps_restricted_list_0

    List restricted apps for an org or workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.apps:read&#x60;
    :type token: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page
    :type cursor: str
    :param team_id: 
    :type team_id: str
    :param enterprise_id: 
    :type enterprise_id: str

    """
    return web.Response(status=200)


async def admin_conversations_archive_0(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_archive_0

    Archive a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to archive.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_convert_to_private_0(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_convert_to_private_0

    Convert a public channel to a private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to convert to private.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_create_0(request: web.Request, token, is_private, name, description=None, org_wide=None, team_id=None) -> web.Response:
    """admin_conversations_create_0

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


async def admin_conversations_delete_0(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_delete_0

    Delete a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to delete.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_disconnect_shared_0(request: web.Request, token, channel_id, leaving_team_ids=None) -> web.Response:
    """admin_conversations_disconnect_shared_0

    Disconnect a connected channel from one or more workspaces.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to be disconnected from some workspaces.
    :type channel_id: str
    :param leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
    :type leaving_team_ids: str

    """
    return web.Response(status=200)


async def admin_conversations_ekm_list_original_connected_channel_info_0(request: web.Request, token, channel_ids=None, team_ids=None, limit=None, cursor=None) -> web.Response:
    """admin_conversations_ekm_list_original_connected_channel_info_0

    List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_ids: A comma-separated list of channels to filter to.
    :type channel_ids: str
    :param team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
    :type team_ids: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str

    """
    return web.Response(status=200)


async def admin_conversations_get_conversation_prefs_0(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_get_conversation_prefs_0

    Get conversation preferences for a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_id: The channel to get preferences for.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_conversations_get_teams_0(request: web.Request, token, channel_id, cursor=None, limit=None) -> web.Response:
    """admin_conversations_get_teams_0

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


async def admin_conversations_invite_0(request: web.Request, token, channel_id, user_ids) -> web.Response:
    """admin_conversations_invite_0

    Invite a user to a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel that the users will be invited to.
    :type channel_id: str
    :param user_ids: The users to invite.
    :type user_ids: str

    """
    return web.Response(status=200)


async def admin_conversations_rename_0(request: web.Request, token, channel_id, name) -> web.Response:
    """admin_conversations_rename_0

    Rename a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to rename.
    :type channel_id: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def admin_conversations_restrict_access_add_group_0(request: web.Request, channel_id, group_id, token, team_id=None) -> web.Response:
    """admin_conversations_restrict_access_add_group_0

    Add an allowlist of IDP groups for accessing a channel

    :param channel_id: The channel to link this group to.
    :type channel_id: str
    :param group_id: The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel.
    :type group_id: str
    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_conversations_restrict_access_list_groups_0(request: web.Request, token, channel_id, team_id=None) -> web.Response:
    """admin_conversations_restrict_access_list_groups_0

    List all IDP Groups linked to a channel

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_id: 
    :type channel_id: str
    :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_conversations_restrict_access_remove_group_0(request: web.Request, channel_id, group_id, team_id, token) -> web.Response:
    """admin_conversations_restrict_access_remove_group_0

    Remove a linked IDP group linked from a private channel

    :param channel_id: The channel to remove the linked group from.
    :type channel_id: str
    :param group_id: The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel.
    :type group_id: str
    :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    :type team_id: str
    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_conversations_search_0(request: web.Request, token, team_ids=None, query=None, limit=None, cursor=None, search_channel_types=None, sort=None, sort_dir=None) -> web.Response:
    """admin_conversations_search_0

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


async def admin_conversations_set_conversation_prefs_0(request: web.Request, token, channel_id, prefs) -> web.Response:
    """admin_conversations_set_conversation_prefs_0

    Set the posting permissions for a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to set the prefs for
    :type channel_id: str
    :param prefs: The prefs for this channel in a stringified JSON format.
    :type prefs: str

    """
    return web.Response(status=200)


async def admin_conversations_set_teams_0(request: web.Request, token, channel_id, org_channel=None, target_team_ids=None, team_id=None) -> web.Response:
    """admin_conversations_set_teams_0

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


async def admin_conversations_unarchive_0(request: web.Request, token, channel_id) -> web.Response:
    """admin_conversations_unarchive_0

    Unarchive a public or private channel.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:write&#x60;
    :type token: str
    :param channel_id: The channel to unarchive.
    :type channel_id: str

    """
    return web.Response(status=200)


async def admin_emoji_add_0(request: web.Request, name, token, url) -> web.Response:
    """admin_emoji_add_0

    Add an emoji.

    :param name: The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best.
    :type url: str

    """
    return web.Response(status=200)


async def admin_emoji_add_alias_0(request: web.Request, alias_for, name, token) -> web.Response:
    """admin_emoji_add_alias_0

    Add an emoji alias.

    :param alias_for: The alias of the emoji.
    :type alias_for: str
    :param name: The name of the emoji to be aliased. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_emoji_list_0(request: web.Request, token, cursor=None, limit=None) -> web.Response:
    """admin_emoji_list_0

    List emoji for an Enterprise Grid organization.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page
    :type cursor: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int

    """
    return web.Response(status=200)


async def admin_emoji_remove_0(request: web.Request, name, token) -> web.Response:
    """admin_emoji_remove_0

    Remove an emoji across an Enterprise Grid organization

    :param name: The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_emoji_rename_0(request: web.Request, name, new_name, token) -> web.Response:
    """admin_emoji_rename_0

    Rename an emoji.

    :param name: The name of the emoji to be renamed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param new_name: The new name of the emoji.
    :type new_name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_invite_requests_approve_0(request: web.Request, token, invite_request_id, team_id=None) -> web.Response:
    """admin_invite_requests_approve_0

    Approve a workspace invite request.

    :param token: Authentication token. Requires scope: &#x60;admin.invites:write&#x60;
    :type token: str
    :param invite_request_id: ID of the request to invite.
    :type invite_request_id: str
    :param team_id: ID for the workspace where the invite request was made.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_invite_requests_approved_list_0(request: web.Request, token, team_id=None, cursor=None, limit=None) -> web.Response:
    """admin_invite_requests_approved_list_0

    List all approved workspace invite requests.

    :param token: Authentication token. Requires scope: &#x60;admin.invites:read&#x60;
    :type token: str
    :param team_id: ID for the workspace where the invite requests were made.
    :type team_id: str
    :param cursor: Value of the &#x60;next_cursor&#x60; field sent as part of the previous API response
    :type cursor: str
    :param limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
    :type limit: int

    """
    return web.Response(status=200)


async def admin_invite_requests_denied_list_0(request: web.Request, token, team_id=None, cursor=None, limit=None) -> web.Response:
    """admin_invite_requests_denied_list_0

    List all denied workspace invite requests.

    :param token: Authentication token. Requires scope: &#x60;admin.invites:read&#x60;
    :type token: str
    :param team_id: ID for the workspace where the invite requests were made.
    :type team_id: str
    :param cursor: Value of the &#x60;next_cursor&#x60; field sent as part of the previous api response
    :type cursor: str
    :param limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive
    :type limit: int

    """
    return web.Response(status=200)


async def admin_invite_requests_deny_0(request: web.Request, token, invite_request_id, team_id=None) -> web.Response:
    """admin_invite_requests_deny_0

    Deny a workspace invite request.

    :param token: Authentication token. Requires scope: &#x60;admin.invites:write&#x60;
    :type token: str
    :param invite_request_id: ID of the request to invite.
    :type invite_request_id: str
    :param team_id: ID for the workspace where the invite request was made.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_invite_requests_list_0(request: web.Request, token, team_id=None, cursor=None, limit=None) -> web.Response:
    """admin_invite_requests_list_0

    List all pending workspace invite requests.

    :param token: Authentication token. Requires scope: &#x60;admin.invites:read&#x60;
    :type token: str
    :param team_id: ID for the workspace where the invite requests were made.
    :type team_id: str
    :param cursor: Value of the &#x60;next_cursor&#x60; field sent as part of the previous API response
    :type cursor: str
    :param limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
    :type limit: int

    """
    return web.Response(status=200)


async def admin_teams_admins_list_0(request: web.Request, token, team_id, limit=None, cursor=None) -> web.Response:
    """admin_teams_admins_list_0

    List all of the admins on a given workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param team_id: 
    :type team_id: str
    :param limit: The maximum number of items to return.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str

    """
    return web.Response(status=200)


async def admin_teams_create_0(request: web.Request, token, team_domain, team_name, team_description=None, team_discoverability=None) -> web.Response:
    """admin_teams_create_0

    Create an Enterprise team.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param team_domain: Team domain (for example, slacksoftballteam).
    :type team_domain: str
    :param team_name: Team name (for example, Slack Softball Team).
    :type team_name: str
    :param team_description: Description for the team.
    :type team_description: str
    :param team_discoverability: Who can join the team. A team&#39;s discoverability can be &#x60;open&#x60;, &#x60;closed&#x60;, &#x60;invite_only&#x60;, or &#x60;unlisted&#x60;.
    :type team_discoverability: str

    """
    return web.Response(status=200)


async def admin_teams_list_0(request: web.Request, token, limit=None, cursor=None) -> web.Response:
    """admin_teams_list_0

    List all teams on an Enterprise organization

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str

    """
    return web.Response(status=200)


async def admin_teams_owners_list_0(request: web.Request, token, team_id, limit=None, cursor=None) -> web.Response:
    """admin_teams_owners_list_0

    List all of the owners on a given workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param team_id: 
    :type team_id: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str

    """
    return web.Response(status=200)


async def admin_teams_settings_info_0(request: web.Request, token, team_id) -> web.Response:
    """admin_teams_settings_info_0

    Fetch information about settings in a workspace

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_default_channels_0(request: web.Request, channel_ids, team_id, token) -> web.Response:
    """admin_teams_settings_set_default_channels_0

    Set the default channels of a workspace.

    :param channel_ids: An array of channel IDs.
    :type channel_ids: str
    :param team_id: ID for the workspace to set the default channel for.
    :type team_id: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_description_0(request: web.Request, token, description, team_id) -> web.Response:
    """admin_teams_settings_set_description_0

    Set the description of a given workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param description: The new description for the workspace.
    :type description: str
    :param team_id: ID for the workspace to set the description for.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_discoverability_0(request: web.Request, token, discoverability, team_id) -> web.Response:
    """admin_teams_settings_set_discoverability_0

    An API method that allows admins to set the discoverability of a given workspace

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param discoverability: This workspace&#39;s discovery setting. It must be set to one of &#x60;open&#x60;, &#x60;invite_only&#x60;, &#x60;closed&#x60;, or &#x60;unlisted&#x60;.
    :type discoverability: str
    :param team_id: The ID of the workspace to set discoverability on.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_icon_0(request: web.Request, image_url, team_id, token) -> web.Response:
    """admin_teams_settings_set_icon_0

    Sets the icon of a workspace.

    :param image_url: Image URL for the icon
    :type image_url: str
    :param team_id: ID for the workspace to set the icon for.
    :type team_id: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_name_0(request: web.Request, token, name, team_id) -> web.Response:
    """admin_teams_settings_set_name_0

    Set the name of a given workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param name: The new name of the workspace.
    :type name: str
    :param team_id: ID for the workspace to set the name for.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_usergroups_add_channels_0(request: web.Request, token, channel_ids, usergroup_id, team_id=None) -> web.Response:
    """admin_usergroups_add_channels_0

    Add one or more default channels to an IDP group.

    :param token: Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60;
    :type token: str
    :param channel_ids: Comma separated string of channel IDs.
    :type channel_ids: str
    :param usergroup_id: ID of the IDP group to add default channels for.
    :type usergroup_id: str
    :param team_id: The workspace to add default channels in.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_usergroups_add_teams_0(request: web.Request, token, team_ids, usergroup_id, auto_provision=None) -> web.Response:
    """admin_usergroups_add_teams_0

    Associate one or more default workspaces with an organization-wide IDP group.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param team_ids: A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token.
    :type team_ids: str
    :param usergroup_id: An encoded usergroup (IDP Group) ID.
    :type usergroup_id: str
    :param auto_provision: When &#x60;true&#x60;, this method automatically creates new workspace accounts for the IDP group members.
    :type auto_provision: bool

    """
    return web.Response(status=200)


async def admin_usergroups_list_channels_0(request: web.Request, token, usergroup_id, team_id=None, include_num_members=None) -> web.Response:
    """admin_usergroups_list_channels_0

    List the channels linked to an org-level IDP group (user group).

    :param token: Authentication token. Requires scope: &#x60;admin.usergroups:read&#x60;
    :type token: str
    :param usergroup_id: ID of the IDP group to list default channels for.
    :type usergroup_id: str
    :param team_id: ID of the the workspace.
    :type team_id: str
    :param include_num_members: Flag to include or exclude the count of members per channel.
    :type include_num_members: bool

    """
    return web.Response(status=200)


async def admin_usergroups_remove_channels_0(request: web.Request, token, channel_ids, usergroup_id) -> web.Response:
    """admin_usergroups_remove_channels_0

    Remove one or more default channels from an org-level IDP group (user group).

    :param token: Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60;
    :type token: str
    :param channel_ids: Comma-separated string of channel IDs
    :type channel_ids: str
    :param usergroup_id: ID of the IDP Group
    :type usergroup_id: str

    """
    return web.Response(status=200)


async def admin_users_assign_0(request: web.Request, token, team_id, user_id, channel_ids=None, is_restricted=None, is_ultra_restricted=None) -> web.Response:
    """admin_users_assign_0

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


async def admin_users_invite_0(request: web.Request, token, channel_ids, email, team_id, custom_message=None, guest_expiration_ts=None, is_restricted=None, is_ultra_restricted=None, real_name=None, resend=None) -> web.Response:
    """admin_users_invite_0

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


async def admin_users_list_0(request: web.Request, token, team_id, cursor=None, limit=None) -> web.Response:
    """admin_users_list_0

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


async def admin_users_remove_0(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_remove_0

    Remove a user from a workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to remove.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_session_invalidate_0(request: web.Request, token, session_id, team_id) -> web.Response:
    """admin_users_session_invalidate_0

    Invalidate a single session for a user by session_id

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param session_id: 
    :type session_id: int
    :param team_id: ID of the team that the session belongs to
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_users_session_reset_0(request: web.Request, token, user_id, mobile_only=None, web_only=None) -> web.Response:
    """admin_users_session_reset_0

    Wipes all valid sessions on all devices for a given user

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param user_id: The ID of the user to wipe sessions for
    :type user_id: str
    :param mobile_only: Only expire mobile sessions (default: false)
    :type mobile_only: bool
    :param web_only: Only expire web sessions (default: false)
    :type web_only: bool

    """
    return web.Response(status=200)


async def admin_users_set_admin_0(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_set_admin_0

    Set an existing guest, regular user, or owner to be an admin user.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to designate as an admin.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_set_expiration_0(request: web.Request, token, expiration_ts, team_id, user_id) -> web.Response:
    """admin_users_set_expiration_0

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


async def admin_users_set_owner_0(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_set_owner_0

    Set an existing guest, regular user, or admin user to be a workspace owner.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: Id of the user to promote to owner.
    :type user_id: str

    """
    return web.Response(status=200)


async def admin_users_set_regular_0(request: web.Request, token, team_id, user_id) -> web.Response:
    """admin_users_set_regular_0

    Set an existing guest user, admin user, or owner to be a regular user.

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param team_id: The ID (&#x60;T1234&#x60;) of the workspace.
    :type team_id: str
    :param user_id: The ID of the user to designate as a regular user.
    :type user_id: str

    """
    return web.Response(status=200)
