from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_type_version_resource import ApplicationTypeVersionResource
from openapi_server.models.application_type_version_resource_list import ApplicationTypeVersionResourceList
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def application_type_versions_create(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, version, api_version, parameters) -> web.Response:
    """Creates or updates a Service Fabric application type version resource.

    Create or update a Service Fabric application type version resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param version: The application type version.
    :type version: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification.
    :type api_version: str
    :param parameters: The application type version resource.
    :type parameters: dict | bytes

    """
    parameters = ApplicationTypeVersionResource.from_dict(parameters)
    return web.Response(status=200)


async def application_type_versions_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, version, api_version) -> web.Response:
    """Deletes a Service Fabric application type version resource.

    Delete a Service Fabric application type version resource with the specified name.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param version: The application type version.
    :type version: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def application_type_versions_get(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, version, api_version) -> web.Response:
    """Gets a Service Fabric application type version resource.

    Get a Service Fabric application type version resource created or in the process of being created in the Service Fabric application type name resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param version: The application type version.
    :type version: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)


async def application_type_versions_list(request: web.Request, subscription_id, resource_group_name, cluster_name, application_type_name, api_version) -> web.Response:
    """Gets the list of application type version resources created in the specified Service Fabric application type name resource.

    Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource.

    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param application_type_name: The name of the application type name resource.
    :type application_type_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification.
    :type api_version: str

    """
    return web.Response(status=200)
