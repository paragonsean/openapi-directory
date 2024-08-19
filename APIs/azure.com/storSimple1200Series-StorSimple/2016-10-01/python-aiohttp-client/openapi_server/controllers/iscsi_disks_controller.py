from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.iscsi_disk import ISCSIDisk
from openapi_server.models.iscsi_disk_list import ISCSIDiskList
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server import util


async def iscsi_disks_create_or_update(request: web.Request, device_name, iscsi_server_name, disk_name, subscription_id, resource_group_name, manager_name, api_version, iscsi_disk) -> web.Response:
    """iscsi_disks_create_or_update

    Creates or updates the iSCSI disk.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
    :param disk_name: The disk name.
    :type disk_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param iscsi_disk: The iSCSI disk.
    :type iscsi_disk: dict | bytes

    """
    iscsi_disk = ISCSIDisk.from_dict(iscsi_disk)
    return web.Response(status=200)


async def iscsi_disks_delete(request: web.Request, device_name, iscsi_server_name, disk_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_disks_delete

    Deletes the iSCSI disk.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
    :param disk_name: The disk name.
    :type disk_name: str
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


async def iscsi_disks_get(request: web.Request, device_name, iscsi_server_name, disk_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_disks_get

    Returns the properties of the specified iSCSI disk name.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
    :param disk_name: The disk name.
    :type disk_name: str
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


async def iscsi_disks_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_disks_list_by_device

    Retrieves all the iSCSI disks in a device.

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


async def iscsi_disks_list_by_iscsi_server(request: web.Request, device_name, iscsi_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_disks_list_by_iscsi_server

    Retrieves all the disks in a iSCSI server.

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


async def iscsi_disks_list_metric_definition(request: web.Request, device_name, iscsi_server_name, disk_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """iscsi_disks_list_metric_definition

    Retrieves metric definitions for all metric aggregated at the iSCSI disk.

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
    :param disk_name: The iSCSI disk name.
    :type disk_name: str
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


async def iscsi_disks_list_metrics(request: web.Request, device_name, iscsi_server_name, disk_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """iscsi_disks_list_metrics

    Gets the iSCSI disk metrics

    :param device_name: The device name.
    :type device_name: str
    :param iscsi_server_name: The iSCSI server name.
    :type iscsi_server_name: str
    :param disk_name: The iSCSI disk name.
    :type disk_name: str
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
