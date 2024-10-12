from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_cluster import VirtualCluster
from openapi_server.models.virtual_cluster_list_result import VirtualClusterListResult
from openapi_server.models.virtual_cluster_update import VirtualClusterUpdate
from openapi_server import util


async def virtual_clusters_delete(request: web.Request, resource_group_name, virtual_cluster_name, subscription_id, api_version) -> web.Response:
    """virtual_clusters_delete

    Deletes a virtual cluster.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param virtual_cluster_name: The name of the virtual cluster.
    :type virtual_cluster_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_clusters_get(request: web.Request, resource_group_name, virtual_cluster_name, subscription_id, api_version) -> web.Response:
    """virtual_clusters_get

    Gets a virtual cluster.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param virtual_cluster_name: The name of the virtual cluster.
    :type virtual_cluster_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_clusters_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """virtual_clusters_list

    Gets a list of all virtualClusters in the subscription.

    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_clusters_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """virtual_clusters_list_by_resource_group

    Gets a list of virtual clusters in a resource group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_clusters_update(request: web.Request, resource_group_name, virtual_cluster_name, subscription_id, api_version, parameters) -> web.Response:
    """virtual_clusters_update

    Updates a virtual cluster.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param virtual_cluster_name: The name of the virtual cluster.
    :type virtual_cluster_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested managed instance resource state.
    :type parameters: dict | bytes

    """
    parameters = VirtualClusterUpdate.from_dict(parameters)
    return web.Response(status=200)
