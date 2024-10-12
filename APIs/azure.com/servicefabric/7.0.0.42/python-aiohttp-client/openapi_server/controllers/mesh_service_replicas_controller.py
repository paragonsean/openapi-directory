from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_service_replica_description_list import PagedServiceReplicaDescriptionList
from openapi_server.models.service_replica_description import ServiceReplicaDescription
from openapi_server import util


async def mesh_service_replica_get(request: web.Request, api_version, application_resource_name, service_resource_name, replica_name) -> web.Response:
    """Gets the given replica of the service of an application.

    Gets the information about the service replica with the given name. The information include the description and other properties of the service replica.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str
    :param replica_name: Service Fabric replica name.
    :type replica_name: str

    """
    return web.Response(status=200)


async def mesh_service_replica_list(request: web.Request, api_version, application_resource_name, service_resource_name) -> web.Response:
    """Lists all the replicas of a service.

    Gets the information about all replicas of a service. The information include the description and other properties of the service replica.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str

    """
    return web.Response(status=200)
