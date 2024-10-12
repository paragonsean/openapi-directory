from typing import List, Dict
from aiohttp import web

from openapi_server.models.clusters_execute_script_actions_default_response import ClustersExecuteScriptActionsDefaultResponse
from openapi_server.models.script_action_execution_history_list import ScriptActionExecutionHistoryList
from openapi_server.models.script_actions_get_execution_detail200_response import ScriptActionsGetExecutionDetail200Response
from openapi_server import util


async def script_actions_get_execution_detail(request: web.Request, subscription_id, resource_group_name, cluster_name, script_execution_id, api_version) -> web.Response:
    """script_actions_get_execution_detail

    Gets the script execution detail for the given script execution ID.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param script_execution_id: The script execution Id
    :type script_execution_id: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def script_execution_history_list(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version) -> web.Response:
    """script_execution_history_list

    Lists all scripts&#39; execution history for the specified cluster.

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
