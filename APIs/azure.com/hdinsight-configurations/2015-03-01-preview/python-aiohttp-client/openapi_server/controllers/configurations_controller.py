from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_configurations import ClusterConfigurations
from openapi_server.models.configurations_list_default_response import ConfigurationsListDefaultResponse
from openapi_server import util


async def configurations_get(request: web.Request, subscription_id, resource_group_name, cluster_name, configuration_name, api_version) -> web.Response:
    """configurations_get

    The configuration object for the specified cluster. This API is not recommended and might be removed in the future. Please consider using List configurations API instead.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param configuration_name: The name of the cluster configuration.
    :type configuration_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def configurations_list(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """configurations_list

    Gets all configuration information for an HDI cluster.

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


async def configurations_update(request: web.Request, subscription_id, resource_group_name, cluster_name, configuration_name, api_version, parameters) -> web.Response:
    """configurations_update

    Configures the HTTP settings on the specified cluster. This API is deprecated, please use UpdateGatewaySettings in cluster endpoint instead.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param configuration_name: The name of the cluster configuration.
    :type configuration_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The cluster configurations.
    :type parameters: Dict[str, str]

    """
    return web.Response(status=200)
