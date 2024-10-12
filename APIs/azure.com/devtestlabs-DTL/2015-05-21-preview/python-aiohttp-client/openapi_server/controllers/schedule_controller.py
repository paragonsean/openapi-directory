from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_schedule import ResponseWithContinuationSchedule
from openapi_server.models.schedule import Schedule
from openapi_server import util


async def schedule_create_or_update_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, schedule) -> web.Response:
    """schedule_create_or_update_resource

    Create or replace an existing schedule. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param schedule: 
    :type schedule: dict | bytes

    """
    schedule = Schedule.from_dict(schedule)
    return web.Response(status=200)


async def schedule_delete_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """schedule_delete_resource

    Delete schedule. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def schedule_execute(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """schedule_execute

    Execute a schedule. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def schedule_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """schedule_get_resource

    Get schedule.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def schedule_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """schedule_list

    List schedules.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)


async def schedule_patch_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, schedule) -> web.Response:
    """schedule_patch_resource

    Modify properties of schedules.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param schedule: 
    :type schedule: dict | bytes

    """
    schedule = Schedule.from_dict(schedule)
    return web.Response(status=200)
