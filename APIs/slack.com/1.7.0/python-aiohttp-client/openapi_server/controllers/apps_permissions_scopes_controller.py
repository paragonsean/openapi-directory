from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_permissions_scopes_list_success_schema import ApiPermissionsScopesListSuccessSchema
from openapi_server.models.apps_permissions_scopes_list_error_schema import AppsPermissionsScopesListErrorSchema
from openapi_server import util


async def apps_permissions_scopes_list(request: web.Request, token) -> web.Response:
    """apps_permissions_scopes_list

    Returns list of scopes this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str

    """
    return web.Response(status=200)
