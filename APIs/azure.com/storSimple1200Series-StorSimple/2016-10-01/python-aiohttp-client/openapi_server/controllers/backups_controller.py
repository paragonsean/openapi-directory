from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_list import BackupList
from openapi_server.models.clone_request import CloneRequest
from openapi_server.models.error import Error
from openapi_server import util


async def backups_clone(request: web.Request, device_name, backup_name, element_name, subscription_id, resource_group_name, manager_name, api_version, clone_request) -> web.Response:
    """backups_clone

    Clones the given backup element to a new disk or share with given details.

    :param device_name: The device name.
    :type device_name: str
    :param backup_name: The backup name.
    :type backup_name: str
    :param element_name: The backup element name.
    :type element_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param clone_request: The clone request.
    :type clone_request: dict | bytes

    """
    clone_request = CloneRequest.from_dict(clone_request)
    return web.Response(status=200)


async def backups_delete(request: web.Request, device_name, backup_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backups_delete

    Deletes the backup.

    :param device_name: The device name.
    :type device_name: str
    :param backup_name: The backup name.
    :type backup_name: str
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


async def backups_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, for_failover=None, filter=None) -> web.Response:
    """backups_list_by_device

    Retrieves all the backups in a device. Can be used to get the backups for failover also.

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
    :param for_failover: Set to true if you need backups which can be used for failover.
    :type for_failover: bool
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def backups_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """backups_list_by_manager

    Retrieves all the backups in a manager.

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
