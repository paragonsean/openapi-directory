from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_apps_approved_list(request: web.Request, token, limit=None, cursor=None, team_id=None, enterprise_id=None) -> web.Response:
    """admin_apps_approved_list

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
