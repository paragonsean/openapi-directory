from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.open_shift_managed_cluster import OpenShiftManagedCluster
from openapi_server.models.open_shift_managed_cluster_list_result import OpenShiftManagedClusterListResult
from openapi_server.models.tags_object import TagsObject
from openapi_server import util


async def open_shift_managed_clusters_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters) -> web.Response:
    """Creates or updates an OpenShift managed cluster.

    Creates or updates a OpenShift managed cluster with the specified configuration for agents and OpenShift version.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the OpenShift managed cluster resource.
    :type resource_name: str
    :param parameters: Parameters supplied to the Create or Update an OpenShift Managed Cluster operation.
    :type parameters: dict | bytes

    """
    parameters = OpenShiftManagedCluster.from_dict(parameters)
    return web.Response(status=200)


async def open_shift_managed_clusters_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Deletes an OpenShift managed cluster.

    Deletes the OpenShift managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the OpenShift managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def open_shift_managed_clusters_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Gets a OpenShift managed cluster.

    Gets the details of the managed OpenShift cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the OpenShift managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def open_shift_managed_clusters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets a list of OpenShift managed clusters in the specified subscription.

    Gets a list of OpenShift managed clusters in the specified subscription. The operation returns properties of each OpenShift managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def open_shift_managed_clusters_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """Lists OpenShift managed clusters in the specified subscription and resource group.

    Lists OpenShift managed clusters in the specified subscription and resource group. The operation returns properties of each OpenShift managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def open_shift_managed_clusters_update_tags(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters) -> web.Response:
    """Updates tags on an OpenShift managed cluster.

    Updates an OpenShift managed cluster with the specified tags.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the OpenShift managed cluster resource.
    :type resource_name: str
    :param parameters: Parameters supplied to the Update OpenShift Managed Cluster Tags operation.
    :type parameters: dict | bytes

    """
    parameters = TagsObject.from_dict(parameters)
    return web.Response(status=200)
