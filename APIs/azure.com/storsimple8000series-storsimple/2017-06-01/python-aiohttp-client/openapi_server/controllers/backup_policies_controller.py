from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_policy import BackupPolicy
from openapi_server.models.backup_policy_list import BackupPolicyList
from openapi_server import util


async def backup_policies_backup_now(request: web.Request, device_name, backup_policy_name, backup_type, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_policies_backup_now

    Backup the backup policy now.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The backup policy name.
    :type backup_policy_name: str
    :param backup_type: The backup Type. This can be cloudSnapshot or localSnapshot.
    :type backup_type: str
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


async def backup_policies_create_or_update(request: web.Request, device_name, backup_policy_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """backup_policies_create_or_update

    Creates or updates the backup policy.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The name of the backup policy to be created/updated.
    :type backup_policy_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The backup policy.
    :type parameters: dict | bytes

    """
    parameters = BackupPolicy.from_dict(parameters)
    return web.Response(status=200)


async def backup_policies_delete(request: web.Request, device_name, backup_policy_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_policies_delete

    Deletes the backup policy.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The name of the backup policy.
    :type backup_policy_name: str
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


async def backup_policies_get(request: web.Request, device_name, backup_policy_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_policies_get

    Gets the properties of the specified backup policy name.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The name of backup policy to be fetched.
    :type backup_policy_name: str
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


async def backup_policies_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_policies_list_by_device

    Gets all the backup policies in a device.

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

    """
    return web.Response(status=200)
