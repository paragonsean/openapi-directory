from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.service_replica_description import ServiceReplicaDescription
from openapi_server.models.service_replica_description_list import ServiceReplicaDescriptionList
from openapi_server import util


async def service_replica_get(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name, service_resource_name, replica_name) -> web.Response:
    """Gets the given replica of the service of an application.

    Gets the information about the service replica with the given name. The information include the description and other properties of the service replica.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str
    :param replica_name: Service Fabric replica name.
    :type replica_name: str

    """
    return web.Response(status=200)


async def service_replica_list(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name, service_resource_name) -> web.Response:
    """Gets replicas of a given service.

    Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str

    """
    return web.Response(status=200)
