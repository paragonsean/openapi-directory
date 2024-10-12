from typing import List, Dict
from aiohttp import web

from openapi_server.models.clusters_execute_script_actions_default_response import ClustersExecuteScriptActionsDefaultResponse
from openapi_server.models.script_actions_list import ScriptActionsList
from openapi_server import util


async def script_actions_delete(request: web.Request, subscription_id, resource_group_name, cluster_name, script_name, api_version) -> web.Response:
    """script_actions_delete

    Deletes a specified persisted script action of the cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param script_name: The name of the script.
    :type script_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def script_actions_list_by_cluster(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """script_actions_list_by_cluster

    Lists all the persisted script actions for the specified cluster.

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
