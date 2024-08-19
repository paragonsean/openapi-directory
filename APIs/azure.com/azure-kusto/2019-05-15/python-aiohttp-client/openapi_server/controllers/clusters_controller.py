from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_check_name_request import ClusterCheckNameRequest
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_update import ClusterUpdate
from openapi_server.models.list_resource_skus_result import ListResourceSkusResult
from openapi_server import util


async def clusters_check_name_availability(request: web.Request, api_version, subscription_id, location, cluster_name) -> web.Response:
    """clusters_check_name_availability

    Checks that the cluster name is valid and is not already in use.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Azure location.
    :type location: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: dict | bytes

    """
    cluster_name = ClusterCheckNameRequest.from_dict(cluster_name)
    return web.Response(status=200)


async def clusters_create_or_update(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version, parameters) -> web.Response:
    """clusters_create_or_update

    Create or update a Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The Kusto cluster parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = Cluster.from_dict(parameters)
    return web.Response(status=200)


async def clusters_delete(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version) -> web.Response:
    """clusters_delete

    Deletes a Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_get(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version) -> web.Response:
    """clusters_get

    Gets a Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """clusters_list

    Lists all Kusto clusters within a subscription.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """clusters_list_by_resource_group

    Lists all Kusto clusters within a resource group.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_list_skus_by_resource(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id) -> web.Response:
    """clusters_list_skus_by_resource

    Returns the SKUs available for the provided resource.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def clusters_start(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version) -> web.Response:
    """clusters_start

    Starts a Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_stop(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version) -> web.Response:
    """clusters_stop

    Stops a Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_update(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version, parameters) -> web.Response:
    """clusters_update

    Update a Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The Kusto cluster parameters supplied to the Update operation.
    :type parameters: dict | bytes

    """
    parameters = ClusterUpdate.from_dict(parameters)
    return web.Response(status=200)
