from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_logs import ContainerLogs
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def code_package_get_container_logs(request: web.Request, subscription_id, resource_group_name, api_version, application_resource_name, service_resource_name, replica_name, code_package_name, tail=None) -> web.Response:
    """Gets the logs from the container.

    Gets the logs for the container of the specified code package of the service replica.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str
    :param replica_name: Service Fabric replica name.
    :type replica_name: str
    :param code_package_name: The name of code package of the service.
    :type code_package_name: str
    :param tail: Number of lines to show from the end of the logs. Default is 100.
    :type tail: int

    """
    return web.Response(status=200)
