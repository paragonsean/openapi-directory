from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_schedule import BackupSchedule
from openapi_server.models.backup_schedule_list import BackupScheduleList
from openapi_server import util


async def backup_schedules_create_or_update(request: web.Request, device_name, backup_policy_name, backup_schedule_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """backup_schedules_create_or_update

    Creates or updates the backup schedule.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The backup policy name.
    :type backup_policy_name: str
    :param backup_schedule_name: The backup schedule name.
    :type backup_schedule_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The backup schedule.
    :type parameters: dict | bytes

    """
    parameters = BackupSchedule.from_dict(parameters)
    return web.Response(status=200)


async def backup_schedules_delete(request: web.Request, device_name, backup_policy_name, backup_schedule_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_schedules_delete

    Deletes the backup schedule.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The backup policy name.
    :type backup_policy_name: str
    :param backup_schedule_name: The name the backup schedule.
    :type backup_schedule_name: str
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


async def backup_schedules_get(request: web.Request, device_name, backup_policy_name, backup_schedule_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_schedules_get

    Gets the properties of the specified backup schedule name.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The backup policy name.
    :type backup_policy_name: str
    :param backup_schedule_name: The name of the backup schedule to be fetched
    :type backup_schedule_name: str
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


async def backup_schedules_list_by_backup_policy(request: web.Request, device_name, backup_policy_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """backup_schedules_list_by_backup_policy

    Gets all the backup schedules in a backup policy.

    :param device_name: The device name
    :type device_name: str
    :param backup_policy_name: The backup policy name.
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
