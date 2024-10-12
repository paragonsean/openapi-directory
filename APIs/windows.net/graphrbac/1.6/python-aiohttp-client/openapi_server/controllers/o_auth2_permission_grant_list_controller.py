from typing import List, Dict
from aiohttp import web

from openapi_server.models.o_auth2_permission_grant_list_result import OAuth2PermissionGrantListResult
from openapi_server import util


async def o_auth2_permission_grant_list(request: web.Request, api_version, tenant_id, filter=None) -> web.Response:
    """o_auth2_permission_grant_list

    Queries OAuth2 permissions grants for the relevant SP ObjectId of an app.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: This is the Service Principal ObjectId associated with the app
    :type filter: str

    """
    return web.Response(status=200)
