from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_create_parameters_extended import ClusterCreateParametersExtended
from openapi_server.models.cluster_disk_encryption_parameters import ClusterDiskEncryptionParameters
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_patch_parameters import ClusterPatchParameters
from openapi_server.models.cluster_resize_parameters import ClusterResizeParameters
from openapi_server.models.clusters_list_default_response import ClustersListDefaultResponse
from openapi_server.models.gateway_settings import GatewaySettings
from openapi_server.models.update_gateway_settings_parameters import UpdateGatewaySettingsParameters
from openapi_server import util


async def clusters_create(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version, parameters) -> web.Response:
    """clusters_create

    Creates a new HDInsight cluster with the specified parameters.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The cluster create request.
    :type parameters: dict | bytes

    """
    parameters = ClusterCreateParametersExtended.from_dict(parameters)
    return web.Response(status=200)


async def clusters_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """clusters_delete

    Deletes the specified HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_get(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """clusters_get

    Gets the specified cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_get_gateway_settings(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """clusters_get_gateway_settings

    Gets the gateway settings for the specified cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """clusters_list

    Lists all the HDInsight clusters under the subscription.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """clusters_list_by_resource_group

    Lists the HDInsight clusters in a resource group.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def clusters_resize(request: web.Request, subscription_id, resource_group_name, cluster_name, role_name, api_version, parameters) -> web.Response:
    """clusters_resize

    Resizes the specified HDInsight cluster to the specified size.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param role_name: The constant value for the roleName
    :type role_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The parameters for the resize operation.
    :type parameters: dict | bytes

    """
    parameters = ClusterResizeParameters.from_dict(parameters)
    return web.Response(status=200)


async def clusters_rotate_disk_encryption_key(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version, parameters) -> web.Response:
    """clusters_rotate_disk_encryption_key

    Rotate disk encryption key of the specified HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The parameters for the disk encryption operation.
    :type parameters: dict | bytes

    """
    parameters = ClusterDiskEncryptionParameters.from_dict(parameters)
    return web.Response(status=200)


async def clusters_update(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version, parameters) -> web.Response:
    """clusters_update

    Patch HDInsight cluster with the specified parameters.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The cluster patch request.
    :type parameters: dict | bytes

    """
    parameters = ClusterPatchParameters.from_dict(parameters)
    return web.Response(status=200)


async def clusters_update_gateway_settings(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version, parameters) -> web.Response:
    """clusters_update_gateway_settings

    Configures the gateway settings on the specified cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The cluster configurations.
    :type parameters: dict | bytes

    """
    parameters = UpdateGatewaySettingsParameters.from_dict(parameters)
    return web.Response(status=200)
