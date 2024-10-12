from typing import List, Dict
from aiohttp import web

from openapi_server.models.clusters_execute_script_actions_default_response import ClustersExecuteScriptActionsDefaultResponse
from openapi_server import util


async def script_execution_history_promote(request: web.Request, subscription_id, resource_group_name, cluster_name, script_execution_id, api_version) -> web.Response:
    """script_execution_history_promote

    Promotes the specified ad-hoc script execution to a persisted script.

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
