from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_target import StorageTarget
from openapi_server.models.storage_targets_result import StorageTargetsResult
from openapi_server import util


async def storage_targets_create(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name, storagetarget=None) -> web.Response:
    """storage_targets_create

    Create/update a storage target.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the storage target may be delayed until the cache is healthy again.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of cache.
    :type cache_name: str
    :param storage_target_name: Name of storage target.
    :type storage_target_name: str
    :param storagetarget: Object containing the definition of a storage target.
    :type storagetarget: dict | bytes

    """
    storagetarget = StorageTarget.from_dict(storagetarget)
    return web.Response(status=200)


async def storage_targets_delete(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name) -> web.Response:
    """storage_targets_delete

    Removes a storage target from a cache.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the storage target may be delayed until the cache is healthy again.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of cache.
    :type cache_name: str
    :param storage_target_name: Name of storage target.
    :type storage_target_name: str

    """
    return web.Response(status=200)


async def storage_targets_get(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name) -> web.Response:
    """storage_targets_get

    Returns a storage target from a cache.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of cache.
    :type cache_name: str
    :param storage_target_name: Name of storage target.
    :type storage_target_name: str

    """
    return web.Response(status=200)


async def storage_targets_list_by_cache(request: web.Request, resource_group_name, api_version, subscription_id, cache_name) -> web.Response:
    """storage_targets_list_by_cache

    Returns the StorageTargets for this cache in the subscription and resource group.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of cache.
    :type cache_name: str

    """
    return web.Response(status=200)


async def storage_targets_update(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, storage_target_name, storagetarget=None) -> web.Response:
    """storage_targets_update

    Update a storage target.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the storage target may be delayed until the cache is healthy again.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of cache.
    :type cache_name: str
    :param storage_target_name: Name of storage target.
    :type storage_target_name: str
    :param storagetarget: Object containing the definition of a storage target.
    :type storagetarget: dict | bytes

    """
    storagetarget = StorageTarget.from_dict(storagetarget)
    return web.Response(status=200)
