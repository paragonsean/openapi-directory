from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_apps_approve(request: web.Request, token, app_id=None, request_id=None, team_id=None) -> web.Response:
    """admin_apps_approve

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


async def admin_apps_restrict(request: web.Request, token, app_id=None, request_id=None, team_id=None) -> web.Response:
    """admin_apps_restrict

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
