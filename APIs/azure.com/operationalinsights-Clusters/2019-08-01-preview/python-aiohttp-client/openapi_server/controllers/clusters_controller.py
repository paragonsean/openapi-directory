from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_patch import ClusterPatch
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def clusters_create_or_update(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """clusters_create_or_update

    Create or update a Log Analytics cluster.

    :param resource_group_name: The resource group name of the Log Analytics cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Log Analytics cluster.
    :type cluster_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters required to create or update a Log Analytics cluster.
    :type parameters: dict | bytes

    """
    parameters = Cluster.from_dict(parameters)
    return web.Response(status=200)


async def clusters_delete(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """clusters_delete

    Deletes a cluster instance.

    :param resource_group_name: The resource group name of the Log Analytics cluster.
    :type resource_group_name: str
    :param cluster_name: Name of the Log Analytics Cluster.
    :type cluster_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_get(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """clusters_get

    Gets a Log Analytics cluster instance.

    :param resource_group_name: The resource group name of the Log Analytics cluster.
    :type resource_group_name: str
    :param cluster_name: Name of the Log Analytics Cluster.
    :type cluster_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """clusters_list

    Gets the Log Analytics clusters in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """clusters_list_by_resource_group

    Gets Log Analytics clusters in a resource group.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_update(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """clusters_update

    Updates a Log Analytics cluster.

    :param resource_group_name: The resource group name of the cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters required to patch a Log Analytics cluster.
    :type parameters: dict | bytes

    """
    parameters = ClusterPatch.from_dict(parameters)
    return web.Response(status=200)
