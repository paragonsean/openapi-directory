from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server import util


async def o_auth2_permission_grant_delete(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """o_auth2_permission_grant_delete

    Delete a OAuth2 permission grant for the relevant resource Ids of an app.

    :param object_id: The object ID of a permission grant.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
