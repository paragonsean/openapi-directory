from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_update_parameters import ClusterUpdateParameters
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def clusters_create_or_update(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """Creates or updates a Service Fabric cluster resource.

    Create or update a Service Fabric cluster resource with the specified name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param parameters: The cluster resource.
    :type parameters: dict | bytes

    """
    parameters = Cluster.from_dict(parameters)
    return web.Response(status=200)


async def clusters_delete(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """Deletes a Service Fabric cluster resource.

    Delete a Service Fabric cluster resource with the specified name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_get(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """Gets a Service Fabric cluster resource.

    Get a Service Fabric cluster resource created or in the process of being created in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets the list of Service Fabric cluster resources created in the specified subscription.

    Gets all Service Fabric cluster resources created or in the process of being created in the subscription.

    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """Gets the list of Service Fabric cluster resources created in the specified resource group.

    Gets all Service Fabric cluster resources created or in the process of being created in the resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_update(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """Updates the configuration of a Service Fabric cluster resource.

    Update the configuration of a Service Fabric cluster resource with the specified name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource.
    :type cluster_name: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param parameters: The parameters which contains the property value and property name which used to update the cluster configuration.
    :type parameters: dict | bytes

    """
    parameters = ClusterUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
