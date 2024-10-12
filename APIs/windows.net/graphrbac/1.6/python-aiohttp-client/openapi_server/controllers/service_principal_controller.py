from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.service_principal import ServicePrincipal
from openapi_server.models.service_principal_create_parameters import ServicePrincipalCreateParameters
from openapi_server.models.service_principal_list_result import ServicePrincipalListResult
from openapi_server.models.service_principal_update_parameters import ServicePrincipalUpdateParameters
from openapi_server import util


async def service_principals_create(request: web.Request, api_version, tenant_id, body) -> web.Response:
    """service_principals_create

    Creates a service principal in the directory.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to create a service principal.
    :type body: dict | bytes

    """
    body = ServicePrincipalCreateParameters.from_dict(body)
    return web.Response(status=200)


async def service_principals_delete(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """service_principals_delete

    Deletes a service principal from the directory.

    :param object_id: The object ID of the service principal to delete.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def service_principals_get(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """service_principals_get

    Gets service principal information from the directory. Query by objectId or pass a filter to query by appId

    :param object_id: The object ID of the service principal to get.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def service_principals_list(request: web.Request, api_version, tenant_id, filter=None) -> web.Response:
    """service_principals_list

    Gets a list of service principals from the current tenant.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: The filter to apply to the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def service_principals_update(request: web.Request, object_id, api_version, tenant_id, body) -> web.Response:
    """service_principals_update

    Updates a service principal in the directory.

    :param object_id: The object ID of the service principal to delete.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update a service principal.
    :type body: dict | bytes

    """
    body = ServicePrincipalUpdateParameters.from_dict(body)
    return web.Response(status=200)
