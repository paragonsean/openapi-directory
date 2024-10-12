from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_permissions_info_error_schema import AppsPermissionsInfoErrorSchema
from openapi_server.models.apps_permissions_info_schema import AppsPermissionsInfoSchema
from openapi_server.models.apps_permissions_request_error_schema import AppsPermissionsRequestErrorSchema
from openapi_server.models.apps_permissions_request_schema import AppsPermissionsRequestSchema
from openapi_server import util


async def apps_permissions_info(request: web.Request, token=None) -> web.Response:
    """apps_permissions_info

    Returns list of permissions this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def apps_permissions_request(request: web.Request, token, scopes, trigger_id) -> web.Response:
    """apps_permissions_request

    Allows an app to request additional scopes

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param scopes: A comma separated list of scopes to request for
    :type scopes: str
    :param trigger_id: Token used to trigger the permissions API
    :type trigger_id: str

    """
    return web.Response(status=200)
