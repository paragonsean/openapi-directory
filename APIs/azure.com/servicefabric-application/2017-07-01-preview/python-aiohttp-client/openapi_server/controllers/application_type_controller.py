from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_type_resource import ApplicationTypeResource
from openapi_server.models.application_type_resource_list import ApplicationTypeResourceList
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def application_types_create(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, api_version, parameters) -> web.Response:
    """Creates or updates a Service Fabric application type name resource.

    Create or update a Service Fabric application type name resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification.
    :type api_version: str
    :param parameters: The application type name resource.
    :type parameters: dict | bytes

    """
    parameters = ApplicationTypeResource.from_dict(parameters)
    return web.Response(status=200)


async def application_types_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, api_version) -> web.Response:
    """Deletes a Service Fabric application type name resource.

    Delete a Service Fabric application type name resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def application_types_get(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, api_version) -> web.Response:
    """Gets a Service Fabric application type name resource.

    Get a Service Fabric application type name resource created or in the process of being created in the Service Fabric cluster resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def application_types_list(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """Gets the list of application type name resources created in the specified Service Fabric cluster resource.

    Gets all application type name resources created or in the process of being created in the Service Fabric cluster resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)
