from typing import List, Dict
from aiohttp import web

from openapi_server.models.redis_patch_schedule import RedisPatchSchedule
from openapi_server.models.redis_patch_schedule_list_result import RedisPatchScheduleListResult
from openapi_server import util


async def patch_schedules_create_or_update_0(request: web.Request, resource_group_name, name, default, api_version, subscription_id, parameters) -> web.Response:
    """patch_schedules_create_or_update_0

    Create or replace the patching schedule for Redis cache (requires Premium SKU).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param default: Default string modeled as parameter for auto generation to work correctly.
    :type default: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to set the patching schedule for Redis cache.
    :type parameters: dict | bytes

    """
    parameters = RedisPatchSchedule.from_dict(parameters)
    return web.Response(status=200)


async def patch_schedules_delete_0(request: web.Request, resource_group_name, name, default, api_version, subscription_id) -> web.Response:
    """patch_schedules_delete_0

    Deletes the patching schedule of a redis cache (requires Premium SKU).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the redis cache.
    :type name: str
    :param default: Default string modeled as parameter for auto generation to work correctly.
    :type default: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def patch_schedules_get_0(request: web.Request, resource_group_name, name, default, api_version, subscription_id) -> web.Response:
    """patch_schedules_get_0

    Gets the patching schedule of a redis cache (requires Premium SKU).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the redis cache.
    :type name: str
    :param default: Default string modeled as parameter for auto generation to work correctly.
    :type default: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def patch_schedules_list_by_redis_resource_0(request: web.Request, api_version, subscription_id, resource_group_name, cache_name) -> web.Response:
    """patch_schedules_list_by_redis_resource_0

    Gets all patch schedules in the specified redis cache (there is only one).

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str

    """
    return web.Response(status=200)
