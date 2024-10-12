from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_resource import ApplicationResource
from openapi_server.models.application_resource_list import ApplicationResourceList
from openapi_server.models.application_resource_update import ApplicationResourceUpdate
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def applications_create(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version, parameters) -> web.Response:
    """Creates or updates a Service Fabric application resource.

    Create or update a Service Fabric application resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification.
    :type api_version: str
    :param parameters: The application resource.
    :type parameters: dict | bytes

    """
    parameters = ApplicationResource.from_dict(parameters)
    return web.Response(status=200)


async def applications_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version) -> web.Response:
    """Deletes a Service Fabric application resource.

    Delete a Service Fabric application resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_get(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version) -> web.Response:
    """Gets a Service Fabric application resource.

    Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_list(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """Gets the list of application resources created in the specified Service Fabric cluster resource.

    Gets all application resources created or in the process of being created in the Service Fabric cluster resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_update(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version, parameters) -> web.Response:
    """Updates a Service Fabric application resource.

    Update a Service Fabric application resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_name: The name of the application resource.
    :type application_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification.
    :type api_version: str
    :param parameters: The application resource for patch operations.
    :type parameters: dict | bytes

    """
    parameters = ApplicationResourceUpdate.from_dict(parameters)
    return web.Response(status=200)
