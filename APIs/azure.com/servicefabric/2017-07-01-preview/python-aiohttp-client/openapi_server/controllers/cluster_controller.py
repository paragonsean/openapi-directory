from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_update_parameters import ClusterUpdateParameters
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def clusters_create(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """Create a ServiceFabric cluster

    Create cluster resource 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource
    :type cluster_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param parameters: The cluster resource.
    :type parameters: dict | bytes

    """
    parameters = Cluster.from_dict(parameters)
    return web.Response(status=200)


async def clusters_delete(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """Delete cluster resource

    Delete cluster resource 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource
    :type cluster_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_get(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """Get cluster resource

    Get cluster resource 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource
    :type cluster_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """List cluster resource

    List cluster resource 

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """List cluster resource by resource group

    List cluster resource by resource group 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_update(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """Update cluster configuration

    Update cluster configuration 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource
    :type cluster_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param parameters: The parameters which contains the property value and property name which used to update the cluster configuration.
    :type parameters: dict | bytes

    """
    parameters = ClusterUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
