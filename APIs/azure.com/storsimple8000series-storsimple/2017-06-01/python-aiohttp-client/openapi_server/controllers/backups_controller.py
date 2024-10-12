from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_list import BackupList
from openapi_server.models.clone_request import CloneRequest
from openapi_server import util


async def backups_clone(request: web.Request, device_name, backup_name, backup_element_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """backups_clone

    Clones the backup element as a new volume.

    :param device_name: The device name
    :type device_name: str
    :param backup_name: The backup name.
    :type backup_name: str
    :param backup_element_name: The backup element name.
    :type backup_element_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The clone request object.
    :type parameters: dict | bytes

    """
    parameters = CloneRequest.from_dict(parameters)
    return web.Response(status=200)


async def backups_delete(request: web.Request, device_name, backup_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backups_delete

    Deletes the backup.

    :param device_name: The device name
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


async def backups_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """backups_list_by_device

    Retrieves all the backups in a device.

    :param device_name: The device name
    :type device_name: str
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


async def backups_restore(request: web.Request, device_name, backup_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backups_restore

    Restores the backup on the device.

    :param device_name: The device name
    :type device_name: str
    :param backup_name: The backupSet name
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
