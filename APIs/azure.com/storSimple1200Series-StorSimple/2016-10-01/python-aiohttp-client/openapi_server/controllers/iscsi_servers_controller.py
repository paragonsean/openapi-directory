from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.iscsi_server import ISCSIServer
from openapi_server.models.iscsi_server_list import ISCSIServerList
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server import util


async def iscsi_servers_backup_now(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_servers_backup_now

    Backup the iSCSI server now.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
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


async def iscsi_servers_create_or_update(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version, iscsi_server) -> web.Response:
    """iscsi_servers_create_or_update

    Creates or updates the iSCSI server.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param iscsi_server: The iSCSI server.
    :type iscsi_server: dict | bytes

    """
    iscsi_server = ISCSIServer.from_dict(iscsi_server)
    return web.Response(status=200)


async def iscsi_servers_delete(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_servers_delete

    Deletes the iSCSI server.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
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


async def iscsi_servers_get(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_servers_get

    Returns the properties of the specified iSCSI server name.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
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


async def iscsi_servers_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_servers_list_by_device

    Retrieves all the iSCSI in a device.

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


async def iscsi_servers_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_servers_list_by_manager

    Retrieves all the iSCSI servers in a manager.

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


async def iscsi_servers_list_metric_definition(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_servers_list_metric_definition

    Retrieves metric definitions for all metrics aggregated at iSCSI server.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
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


async def iscsi_servers_list_metrics(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """iscsi_servers_list_metrics

    Gets the iSCSI server metrics

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
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
