from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_invite_requests_approved_list(request: web.Request, token, team_id=None, cursor=None, limit=None) -> web.Response:
    """admin_invite_requests_approved_list

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
