from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_teams_settings_info(request: web.Request, token, team_id) -> web.Response:
    """admin_teams_settings_info

    Fetch information about settings in a workspace

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_default_channels(request: web.Request, channel_ids, team_id, token) -> web.Response:
    """admin_teams_settings_set_default_channels

    Set the default channels of a workspace.

    :param channel_ids: An array of channel IDs.
    :type channel_ids: str
    :param team_id: ID for the workspace to set the default channel for.
    :type team_id: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_description(request: web.Request, token, description, team_id) -> web.Response:
    """admin_teams_settings_set_description

    Set the description of a given workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param description: The new description for the workspace.
    :type description: str
    :param team_id: ID for the workspace to set the description for.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_discoverability(request: web.Request, token, discoverability, team_id) -> web.Response:
    """admin_teams_settings_set_discoverability

    An API method that allows admins to set the discoverability of a given workspace

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param discoverability: This workspace&#39;s discovery setting. It must be set to one of &#x60;open&#x60;, &#x60;invite_only&#x60;, &#x60;closed&#x60;, or &#x60;unlisted&#x60;.
    :type discoverability: str
    :param team_id: The ID of the workspace to set discoverability on.
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_icon(request: web.Request, image_url, team_id, token) -> web.Response:
    """admin_teams_settings_set_icon

    Sets the icon of a workspace.

    :param image_url: Image URL for the icon
    :type image_url: str
    :param team_id: ID for the workspace to set the icon for.
    :type team_id: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_teams_settings_set_name(request: web.Request, token, name, team_id) -> web.Response:
    """admin_teams_settings_set_name

    Set the name of a given workspace.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param name: The new name of the workspace.
    :type name: str
    :param team_id: ID for the workspace to set the name for.
    :type team_id: str

    """
    return web.Response(status=200)
