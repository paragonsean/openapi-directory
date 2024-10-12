from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_target import StorageTarget
from openapi_server.models.storage_targets_result import StorageTargetsResult
from openapi_server import util


async def storage_targets_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name, storagetarget=None) -> web.Response:
    """storage_targets_create_or_update

    Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param storage_target_name: Name of the Storage Target.
    :type storage_target_name: str
    :param storagetarget: Object containing the definition of a Storage Target.
    :type storagetarget: dict | bytes

    """
    storagetarget = StorageTarget.from_dict(storagetarget)
    return web.Response(status=200)


async def storage_targets_delete(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name) -> web.Response:
    """storage_targets_delete

    Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param storage_target_name: Name of Storage Target.
    :type storage_target_name: str

    """
    return web.Response(status=200)


async def storage_targets_get(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name) -> web.Response:
    """storage_targets_get

    Returns a Storage Target from a Cache.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param storage_target_name: Name of the Storage Target.
    :type storage_target_name: str

    """
    return web.Response(status=200)


async def storage_targets_list_by_cache(request: web.Request, resource_group_name, api_version, subscription_id, cache_name) -> web.Response:
    """storage_targets_list_by_cache

    Returns a list of Storage Targets for the specified Cache.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of Cache.
    :type cache_name: str

    """
    return web.Response(status=200)
