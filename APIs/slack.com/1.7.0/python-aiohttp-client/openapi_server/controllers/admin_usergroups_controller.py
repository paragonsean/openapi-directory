from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_usergroups_add_channels(request: web.Request, token, channel_ids, usergroup_id, team_id=None) -> web.Response:
    """admin_usergroups_add_channels

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


async def admin_usergroups_add_teams(request: web.Request, token, team_ids, usergroup_id, auto_provision=None) -> web.Response:
    """admin_usergroups_add_teams

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


async def admin_usergroups_list_channels(request: web.Request, token, usergroup_id, team_id=None, include_num_members=None) -> web.Response:
    """admin_usergroups_list_channels

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


async def admin_usergroups_remove_channels(request: web.Request, token, channel_ids, usergroup_id) -> web.Response:
    """admin_usergroups_remove_channels

    Remove one or more default channels from an org-level IDP group (user group).

    :param token: Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60;
    :type token: str
    :param channel_ids: Comma-separated string of channel IDs
    :type channel_ids: str
    :param usergroup_id: ID of the IDP Group
    :type usergroup_id: str

    """
    return web.Response(status=200)
