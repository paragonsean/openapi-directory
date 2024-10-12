from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.service_resource import ServiceResource
from openapi_server.models.service_resource_list import ServiceResourceList
from openapi_server.models.service_resource_update import ServiceResourceUpdate
from openapi_server import util


async def services_create_or_update(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, service_name, api_version, parameters) -> web.Response:
    """Creates or updates a Service Fabric service resource.

    Create or update a Service Fabric service resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
    :type service_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param parameters: The service resource.
    :type parameters: dict | bytes

    """
    parameters = ServiceResource.from_dict(parameters)
    return web.Response(status=200)


async def services_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, service_name, api_version) -> web.Response:
    """Deletes a Service Fabric service resource.

    Delete a Service Fabric service resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
    :type service_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_get(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, service_name, api_version) -> web.Response:
    """Gets a Service Fabric service resource.

    Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
    :type service_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version) -> web.Response:
    """Gets the list of service resources created in the specified Service Fabric application resource.

    Gets all service resources created or in the process of being created in the Service Fabric application resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_update(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, service_name, api_version, parameters) -> web.Response:
    """Updates a Service Fabric service resource.

    Update a Service Fabric service resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
    :type service_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param parameters: The service resource for patch operations.
    :type parameters: dict | bytes

    """
    parameters = ServiceResourceUpdate.from_dict(parameters)
    return web.Response(status=200)
