from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_teams_create(request: web.Request, token, team_domain, team_name, team_description=None, team_discoverability=None) -> web.Response:
    """admin_teams_create

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


async def admin_teams_list(request: web.Request, token, limit=None, cursor=None) -> web.Response:
    """admin_teams_list

    List all teams on an Enterprise organization

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str

    """
    return web.Response(status=200)
