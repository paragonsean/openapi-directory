from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_monitor import ConnectionMonitor
from openapi_server.models.connection_monitor_list_result import ConnectionMonitorListResult
from openapi_server.models.connection_monitor_query_result import ConnectionMonitorQueryResult
from openapi_server.models.connection_monitor_result import ConnectionMonitorResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def connection_monitors_create_or_update(request: web.Request, resource_group_name, network_watcher_name, connection_monitor_name, api_version, subscription_id, parameters) -> web.Response:
    """connection_monitors_create_or_update

    Create or update a connection monitor.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param connection_monitor_name: The name of the connection monitor.
    :type connection_monitor_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the operation to create a connection monitor.
    :type parameters: dict | bytes

    """
    parameters = ConnectionMonitor.from_dict(parameters)
    return web.Response(status=200)


async def connection_monitors_delete(request: web.Request, resource_group_name, network_watcher_name, connection_monitor_name, api_version, subscription_id) -> web.Response:
    """connection_monitors_delete

    Deletes the specified connection monitor.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param connection_monitor_name: The name of the connection monitor.
    :type connection_monitor_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connection_monitors_get(request: web.Request, resource_group_name, network_watcher_name, connection_monitor_name, api_version, subscription_id) -> web.Response:
    """connection_monitors_get

    Gets a connection monitor by name.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param connection_monitor_name: The name of the connection monitor.
    :type connection_monitor_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connection_monitors_list(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id) -> web.Response:
    """connection_monitors_list

    Lists all connection monitors for the specified Network Watcher.

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


async def connection_monitors_query(request: web.Request, resource_group_name, network_watcher_name, connection_monitor_name, api_version, subscription_id) -> web.Response:
    """connection_monitors_query

    Query a snapshot of the most recent connection states.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param connection_monitor_name: The name given to the connection monitor.
    :type connection_monitor_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connection_monitors_start(request: web.Request, resource_group_name, network_watcher_name, connection_monitor_name, api_version, subscription_id) -> web.Response:
    """connection_monitors_start

    Starts the specified connection monitor.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param connection_monitor_name: The name of the connection monitor.
    :type connection_monitor_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connection_monitors_stop(request: web.Request, resource_group_name, network_watcher_name, connection_monitor_name, api_version, subscription_id) -> web.Response:
    """connection_monitors_stop

    Stops the specified connection monitor.

    :param resource_group_name: The name of the resource group containing Network Watcher.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param connection_monitor_name: The name of the connection monitor.
    :type connection_monitor_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
