from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_schedule_group import BackupScheduleGroup
from openapi_server.models.backup_schedule_group_list import BackupScheduleGroupList
from openapi_server.models.error import Error
from openapi_server import util


async def backup_schedule_groups_create_or_update(request: web.Request, device_name, schedule_group_name, subscription_id, resource_group_name, manager_name, api_version, schedule_group) -> web.Response:
    """backup_schedule_groups_create_or_update

    Creates or Updates the backup schedule Group.

    :param device_name: The name of the device.
    :type device_name: str
    :param schedule_group_name: The name of the schedule group.
    :type schedule_group_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param schedule_group: The schedule group to be created
    :type schedule_group: dict | bytes

    """
    schedule_group = BackupScheduleGroup.from_dict(schedule_group)
    return web.Response(status=200)


async def backup_schedule_groups_delete(request: web.Request, device_name, schedule_group_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_schedule_groups_delete

    Deletes the backup schedule group.

    :param device_name: The name of the device.
    :type device_name: str
    :param schedule_group_name: The name of the schedule group.
    :type schedule_group_name: str
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


async def backup_schedule_groups_get(request: web.Request, device_name, schedule_group_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_schedule_groups_get

    Returns the properties of the specified backup schedule group name.

    :param device_name: The name of the device.
    :type device_name: str
    :param schedule_group_name: The name of the schedule group.
    :type schedule_group_name: str
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


async def backup_schedule_groups_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_schedule_groups_list_by_device

    Retrieves all the backup schedule groups in a device.

    :param device_name: The name of the device.
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
