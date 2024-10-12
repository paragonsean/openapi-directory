from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_role_assignment_list_result import AppRoleAssignmentListResult
from openapi_server.models.graph_error import GraphError
from openapi_server import util


async def service_principals_list_app_role_assigned_to(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """Principals (users, groups, and service principals) that are assigned to this service principal.

    

    :param object_id: The object ID of the service principal for which to get owners.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
