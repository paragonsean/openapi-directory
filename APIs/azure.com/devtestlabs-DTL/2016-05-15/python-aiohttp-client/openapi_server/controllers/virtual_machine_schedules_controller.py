from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_schedule import ResponseWithContinuationSchedule
from openapi_server.models.schedule import Schedule
from openapi_server.models.schedule_fragment import ScheduleFragment
from openapi_server import util


async def virtual_machine_schedules_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, virtual_machine_name, name, api_version, schedule) -> web.Response:
    """virtual_machine_schedules_create_or_update

    Create or replace an existing schedule.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param virtual_machine_name: The name of the virtual machine.
    :type virtual_machine_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param schedule: A schedule.
    :type schedule: dict | bytes

    """
    schedule = Schedule.from_dict(schedule)
    return web.Response(status=200)


async def virtual_machine_schedules_delete(request: web.Request, subscription_id, resource_group_name, lab_name, virtual_machine_name, name, api_version) -> web.Response:
    """virtual_machine_schedules_delete

    Delete schedule.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param virtual_machine_name: The name of the virtual machine.
    :type virtual_machine_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_schedules_execute(request: web.Request, subscription_id, resource_group_name, lab_name, virtual_machine_name, name, api_version) -> web.Response:
    """virtual_machine_schedules_execute

    Execute a schedule. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param virtual_machine_name: The name of the virtual machine.
    :type virtual_machine_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_schedules_get(request: web.Request, subscription_id, resource_group_name, lab_name, virtual_machine_name, name, api_version, expand=None) -> web.Response:
    """virtual_machine_schedules_get

    Get schedule.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param virtual_machine_name: The name of the virtual machine.
    :type virtual_machine_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machine_schedules_list(request: web.Request, subscription_id, resource_group_name, lab_name, virtual_machine_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """virtual_machine_schedules_list

    List schedules in a given virtual machine.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param virtual_machine_name: The name of the virtual machine.
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def virtual_machine_schedules_update(request: web.Request, subscription_id, resource_group_name, lab_name, virtual_machine_name, name, api_version, schedule) -> web.Response:
    """virtual_machine_schedules_update

    Modify properties of schedules.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param virtual_machine_name: The name of the virtual machine.
    :type virtual_machine_name: str
    :param name: The name of the schedule.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param schedule: A schedule.
    :type schedule: dict | bytes

    """
    schedule = ScheduleFragment.from_dict(schedule)
    return web.Response(status=200)
