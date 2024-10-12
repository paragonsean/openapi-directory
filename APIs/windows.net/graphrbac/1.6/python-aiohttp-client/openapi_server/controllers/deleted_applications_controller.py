from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.graph_error import GraphError
from openapi_server import util


async def deleted_applications_list(request: web.Request, api_version, tenant_id, filter=None) -> web.Response:
    """deleted_applications_list

    Gets a list of deleted applications in the directory.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: The filter to apply to the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def deleted_applications_restore(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """deleted_applications_restore

    Restores the deleted application in the directory.

    :param object_id: Application object ID.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
