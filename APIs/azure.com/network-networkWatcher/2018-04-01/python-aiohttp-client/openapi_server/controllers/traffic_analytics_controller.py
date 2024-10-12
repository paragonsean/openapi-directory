from typing import List, Dict
from aiohttp import web

from openapi_server.models.flow_log_information import FlowLogInformation
from openapi_server.models.flow_log_status_parameters import FlowLogStatusParameters
from openapi_server import util


async def network_watchers_get_flow_log_status_0(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_flow_log_status_0

    Queries status of flow log and traffic analytics (optional) on a specified resource.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define a resource to query flow log and traffic analytics (optional)  status.
    :type parameters: dict | bytes

    """
    parameters = FlowLogStatusParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_set_flow_log_configuration_0(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_set_flow_log_configuration_0

    Configures flow log  and traffic analytics (optional) on a specified resource.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the configuration of flow log.
    :type parameters: dict | bytes

    """
    parameters = FlowLogInformation.from_dict(parameters)
    return web.Response(status=200)
