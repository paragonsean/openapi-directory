from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_conversations_restrict_access_add_group(request: web.Request, channel_id, group_id, token, team_id=None) -> web.Response:
    """admin_conversations_restrict_access_add_group

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


async def admin_conversations_restrict_access_list_groups(request: web.Request, token, channel_id, team_id=None) -> web.Response:
    """admin_conversations_restrict_access_list_groups

    List all IDP Groups linked to a channel

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_id: 
    :type channel_id: str
    :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_conversations_restrict_access_remove_group(request: web.Request, channel_id, group_id, team_id, token) -> web.Response:
    """admin_conversations_restrict_access_remove_group

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
