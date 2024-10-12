from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.applications_list_by_cluster_default_response import ApplicationsListByClusterDefaultResponse
from openapi_server import util


async def applications_create(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version, parameters) -> web.Response:
    """applications_create

    Creates applications for the HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param application_name: The constant value for the application name.
    :type application_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The application create request.
    :type parameters: dict | bytes

    """
    parameters = Application.from_dict(parameters)
    return web.Response(status=200)


async def applications_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version) -> web.Response:
    """applications_delete

    Deletes the specified application on the HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param application_name: The constant value for the application name.
    :type application_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_get(request: web.Request, subscription_id, resource_group_name, cluster_name, application_name, api_version) -> web.Response:
    """applications_get

    Gets properties of the specified application.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param application_name: The constant value for the application name.
    :type application_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_list_by_cluster(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """applications_list_by_cluster

    Lists all of the applications for the HDInsight cluster.

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
