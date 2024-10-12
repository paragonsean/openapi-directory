from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_create_parameters import ApplicationCreateParameters
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.application_update_parameters import ApplicationUpdateParameters
from openapi_server.models.graph_error import GraphError
from openapi_server import util


async def applications_create(request: web.Request, api_version, tenant_id, body) -> web.Response:
    """applications_create

    Create a new application.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: The parameters for creating an application.
    :type body: dict | bytes

    """
    body = ApplicationCreateParameters.from_dict(body)
    return web.Response(status=200)


async def applications_delete(request: web.Request, application_object_id, api_version, tenant_id) -> web.Response:
    """applications_delete

    Delete an application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def applications_get(request: web.Request, application_object_id, api_version, tenant_id) -> web.Response:
    """applications_get

    Get an application by object ID.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def applications_list(request: web.Request, api_version, tenant_id, filter=None) -> web.Response:
    """applications_list

    Lists applications by filter parameters.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: The filters to apply to the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def applications_patch(request: web.Request, application_object_id, api_version, tenant_id, body) -> web.Response:
    """applications_patch

    Update an existing application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update an existing application.
    :type body: dict | bytes

    """
    body = ApplicationUpdateParameters.from_dict(body)
    return web.Response(status=200)


async def deleted_applications_hard_delete(request: web.Request, application_object_id, api_version, tenant_id) -> web.Response:
    """deleted_applications_hard_delete

    Hard-delete an application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
