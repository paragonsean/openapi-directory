from typing import List, Dict
from aiohttp import web

from openapi_server.models.clusters_execute_script_actions_default_response import ClustersExecuteScriptActionsDefaultResponse
from openapi_server.models.clusters_execute_script_actions_request import ClustersExecuteScriptActionsRequest
from openapi_server import util


async def clusters_execute_script_actions(request: web.Request, subscription_id, resource_group_name, cluster_name, api_version, parameters) -> web.Response:
    """clusters_execute_script_actions

    Executes script actions on the specified HDInsight cluster.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param parameters: The parameters for executing script actions.
    :type parameters: dict | bytes

    """
    parameters = ClustersExecuteScriptActionsRequest.from_dict(parameters)
    return web.Response(status=200)
