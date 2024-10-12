from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.service_principal_object_result import ServicePrincipalObjectResult
from openapi_server import util


async def applications_get_service_principals_id_by_app_id(request: web.Request, api_version, tenant_id, application_id) -> web.Response:
    """applications_get_service_principals_id_by_app_id

    Gets an object id for a given application id from the current tenant.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param application_id: The application ID.
    :type application_id: str

    """
    return web.Response(status=200)
