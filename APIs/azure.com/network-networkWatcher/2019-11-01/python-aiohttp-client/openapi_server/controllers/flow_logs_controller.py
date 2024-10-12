from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_monitors_list_default_response import ConnectionMonitorsListDefaultResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.flow_log import FlowLog
from openapi_server.models.flow_log_list_result import FlowLogListResult
from openapi_server import util


async def flow_logs_create_or_update(request: web.Request, resource_group_name, network_watcher_name, flow_log_name, api_version, subscription_id, parameters) -> web.Response:
    """flow_logs_create_or_update

    Create or update a flow log for the specified network security group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param flow_log_name: The name of the flow log.
    :type flow_log_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the create or update flow log resource.
    :type parameters: dict | bytes

    """
    parameters = FlowLog.from_dict(parameters)
    return web.Response(status=200)


async def flow_logs_delete(request: web.Request, resource_group_name, network_watcher_name, flow_log_name, api_version, subscription_id) -> web.Response:
    """flow_logs_delete

    Deletes the specified flow log resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param flow_log_name: The name of the flow log resource.
    :type flow_log_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def flow_logs_get(request: web.Request, resource_group_name, network_watcher_name, flow_log_name, api_version, subscription_id) -> web.Response:
    """flow_logs_get

    Gets a flow log resource by name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param flow_log_name: The name of the flow log resource.
    :type flow_log_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def flow_logs_list(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id) -> web.Response:
    """flow_logs_list

    Lists all flow log resources for the specified Network Watcher.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
