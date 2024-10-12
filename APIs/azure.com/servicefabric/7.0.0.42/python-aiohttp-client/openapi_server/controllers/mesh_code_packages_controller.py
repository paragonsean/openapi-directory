from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_logs import ContainerLogs
from openapi_server.models.fabric_error import FabricError
from openapi_server import util


async def mesh_code_package_get_container_logs(request: web.Request, api_version, application_resource_name, service_resource_name, replica_name, code_package_name, tail=None) -> web.Response:
    """Gets the logs from the container.

    Gets the logs for the container of the specified code package of the service replica.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str
    :param replica_name: Service Fabric replica name.
    :type replica_name: str
    :param code_package_name: The name of code package of the service.
    :type code_package_name: str
    :param tail: Number of lines to show from the end of the logs. Default is 100. &#39;all&#39; to show the complete logs.
    :type tail: str

    """
    return web.Response(status=200)
