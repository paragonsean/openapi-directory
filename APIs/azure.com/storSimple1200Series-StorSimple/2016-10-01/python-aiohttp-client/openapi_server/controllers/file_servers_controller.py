from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.file_server import FileServer
from openapi_server.models.file_server_list import FileServerList
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server import util


async def file_servers_backup_now(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_servers_backup_now

    Backup the file server now.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def file_servers_create_or_update(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version, file_server) -> web.Response:
    """file_servers_create_or_update

    Creates or updates the file server.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param file_server: The file server.
    :type file_server: dict | bytes

    """
    file_server = FileServer.from_dict(file_server)
    return web.Response(status=200)


async def file_servers_delete(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_servers_delete

    Deletes the file server.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def file_servers_get(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_servers_get

    Returns the properties of the specified file server name.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def file_servers_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_servers_list_by_device

    Retrieves all the file servers in a device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def file_servers_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_servers_list_by_manager

    Retrieves all the file servers in a manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def file_servers_list_metric_definition(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_servers_list_metric_definition

    Retrieves metric definitions of all metrics aggregated at the file server.

    :param device_name: The name of the device.
    :type device_name: str
    :param file_server_name: The name of the file server.
    :type file_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def file_servers_list_metrics(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """file_servers_list_metrics

    Gets the file server metrics.

    :param device_name: The name of the device.
    :type device_name: str
    :param file_server_name: The name of the file server name.
    :type file_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)
