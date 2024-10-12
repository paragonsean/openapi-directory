from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_service_resource_description_list import PagedServiceResourceDescriptionList
from openapi_server.models.paged_service_resource_replica_description_list import PagedServiceResourceReplicaDescriptionList
from openapi_server.models.service_resource_description import ServiceResourceDescription
from openapi_server.models.service_resource_replica_description import ServiceResourceReplicaDescription
from openapi_server import util


async def create_application_resource(request: web.Request, api_version, application_resource_name, application_resource_description) -> web.Response:
    """Creates or updates an application resource.

    Creates an application with the specified name and description. If an application with the same name already exists, then its description are updated to the one indicated in this request.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str
    :param application_resource_description: Description for creating an application resource.
    :type application_resource_description: dict | bytes

    """
    application_resource_description = ApplicationResourceDescription.from_dict(application_resource_description)
    return web.Response(status=200)


async def delete_application_resource(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Deletes the specified application.

    Deletes the application identified by the name.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def get_application_resource(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Gets the application with the given name.

    Gets the application with the given name. This includes the information about the application&#39;s services and other runtime information.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def get_replica(request: web.Request, api_version, application_resource_name, service_resource_name, replica_name) -> web.Response:
    """Gets a specific replica of a given service in an application resource.

    Gets the information about the specified replica of a given service of an application. The information includes the runtime properties of the replica instance.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str
    :param service_resource_name: Service Fabric service resource name.
    :type service_resource_name: str
    :param replica_name: Service Fabric replica name.
    :type replica_name: str

    """
    return web.Response(status=200)


async def get_replicas(request: web.Request, api_version, application_resource_name, service_resource_name) -> web.Response:
    """Gets replicas of a given service in an application resource.

    Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str
    :param service_resource_name: Service Fabric service resource name.
    :type service_resource_name: str

    """
    return web.Response(status=200)


async def get_service(request: web.Request, api_version, application_resource_name, service_resource_name) -> web.Response:
    """Gets the description of the specified service in an application resource.

    Gets the description of the service resource.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str
    :param service_resource_name: Service Fabric service resource name.
    :type service_resource_name: str

    """
    return web.Response(status=200)


async def get_services(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Gets all the services in the application resource.

    The operation returns the service descriptions of all the services in the application resource. 

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param application_resource_name: Service Fabric application resource name.
    :type application_resource_name: str

    """
    return web.Response(status=200)
