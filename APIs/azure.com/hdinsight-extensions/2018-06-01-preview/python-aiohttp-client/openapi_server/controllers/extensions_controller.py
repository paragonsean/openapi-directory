from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_monitoring_request import ClusterMonitoringRequest
from openapi_server.models.cluster_monitoring_response import ClusterMonitoringResponse
from openapi_server.models.extension import Extension
from openapi_server.models.extensions_get_monitoring_status_default_response import ExtensionsGetMonitoringStatusDefaultResponse
from openapi_server import util


async def extensions_create(request: web.Request, subscription_id, resource_group_name, cluster_name, extension_name, api_version, parameters) -> web.Response:
    """extensions_create

    Creates an HDInsight cluster extension.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param extension_name: The name of the cluster extension.
    :type extension_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The cluster extensions create request.
    :type parameters: dict | bytes

    """
    parameters = Extension.from_dict(parameters)
    return web.Response(status=200)


async def extensions_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, extension_name, api_version) -> web.Response:
    """extensions_delete

    Deletes the specified extension for HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param extension_name: The name of the cluster extension.
    :type extension_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def extensions_disable_monitoring(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """extensions_disable_monitoring

    Disables the Operations Management Suite (OMS) on the HDInsight cluster.

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


async def extensions_enable_monitoring(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version, parameters) -> web.Response:
    """extensions_enable_monitoring

    Enables the Operations Management Suite (OMS) on the HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The Operations Management Suite (OMS) workspace parameters.
    :type parameters: dict | bytes

    """
    parameters = ClusterMonitoringRequest.from_dict(parameters)
    return web.Response(status=200)


async def extensions_get(request: web.Request, subscription_id, resource_group_name, cluster_name, extension_name, api_version) -> web.Response:
    """extensions_get

    Gets the extension properties for the specified HDInsight cluster extension.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param extension_name: The name of the cluster extension.
    :type extension_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def extensions_get_monitoring_status(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """extensions_get_monitoring_status

    Gets the status of Operations Management Suite (OMS) on the HDInsight cluster.

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
