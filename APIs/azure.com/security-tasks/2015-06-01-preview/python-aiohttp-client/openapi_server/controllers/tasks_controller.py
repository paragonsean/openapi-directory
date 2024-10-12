from typing import List, Dict
from aiohttp import web

from openapi_server.models.security_task import SecurityTask
from openapi_server.models.security_task_list import SecurityTaskList
from openapi_server.models.tasks_list_by_home_region_default_response import TasksListByHomeRegionDefaultResponse
from openapi_server import util


async def tasks_get_resource_group_level_task(request: web.Request, api_version, subscription_id, resource_group_name, asc_location, task_name) -> web.Response:
    """tasks_get_resource_group_level_task

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param task_name: Name of the task object, will be a GUID
    :type task_name: str

    """
    return web.Response(status=200)


async def tasks_get_subscription_level_task(request: web.Request, api_version, subscription_id, asc_location, task_name) -> web.Response:
    """tasks_get_subscription_level_task

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param task_name: Name of the task object, will be a GUID
    :type task_name: str

    """
    return web.Response(status=200)


async def tasks_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """tasks_list

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param filter: OData filter. Optional.
    :type filter: str

    """
    return web.Response(status=200)


async def tasks_list_by_home_region(request: web.Request, api_version, subscription_id, asc_location, filter=None) -> web.Response:
    """tasks_list_by_home_region

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param filter: OData filter. Optional.
    :type filter: str

    """
    return web.Response(status=200)


async def tasks_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, asc_location, filter=None) -> web.Response:
    """tasks_list_by_resource_group

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param filter: OData filter. Optional.
    :type filter: str

    """
    return web.Response(status=200)


async def tasks_update_resource_group_level_task_state(request: web.Request, api_version, subscription_id, resource_group_name, asc_location, task_name, task_update_action_type) -> web.Response:
    """tasks_update_resource_group_level_task_state

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param task_name: Name of the task object, will be a GUID
    :type task_name: str
    :param task_update_action_type: Type of the action to do on the task
    :type task_update_action_type: str

    """
    return web.Response(status=200)


async def tasks_update_subscription_level_task_state(request: web.Request, api_version, subscription_id, asc_location, task_name, task_update_action_type) -> web.Response:
    """tasks_update_subscription_level_task_state

    Recommended tasks that will help improve the security of the subscription proactively

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param task_name: Name of the task object, will be a GUID
    :type task_name: str
    :param task_update_action_type: Type of the action to do on the task
    :type task_update_action_type: str

    """
    return web.Response(status=200)
