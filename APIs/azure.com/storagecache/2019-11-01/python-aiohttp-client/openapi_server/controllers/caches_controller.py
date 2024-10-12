from typing import List, Dict
from aiohttp import web

from openapi_server.models.cache import Cache
from openapi_server.models.caches_list_result import CachesListResult
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def caches_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, cache=None) -> web.Response:
    """caches_create_or_update

    Create or update a Cache.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param cache: Object containing the user-selectable properties of the new Cache. If read-only properties are included, they must match the existing values of those properties.
    :type cache: dict | bytes

    """
    cache = Cache.from_dict(cache)
    return web.Response(status=200)


async def caches_delete(request: web.Request, resource_group_name, cache_name, api_version, subscription_id) -> web.Response:
    """caches_delete

    Schedules a Cache for deletion.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def caches_flush(request: web.Request, resource_group_name, api_version, subscription_id, cache_name) -> web.Response:
    """caches_flush

    Tells a Cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete.

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


async def caches_get(request: web.Request, resource_group_name, cache_name, api_version, subscription_id) -> web.Response:
    """caches_get

    Returns a Cache.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def caches_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """caches_list

    Returns all Caches the user has access to under a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def caches_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """caches_list_by_resource_group

    Returns all Caches the user has access to under a resource group.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def caches_start(request: web.Request, resource_group_name, api_version, subscription_id, cache_name) -> web.Response:
    """caches_start

    Tells a Stopped state Cache to transition to Active state.

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


async def caches_stop(request: web.Request, resource_group_name, api_version, subscription_id, cache_name) -> web.Response:
    """caches_stop

    Tells an Active Cache to transition to Stopped state.

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


async def caches_update(request: web.Request, resource_group_name, api_version, subscription_id, cache_name, cache=None) -> web.Response:
    """caches_update

    Update a Cache instance.

    :param resource_group_name: Target resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cache_name: Name of Cache.
    :type cache_name: str
    :param cache: Object containing the user-selectable properties of the Cache. If read-only properties are included, they must match the existing values of those properties.
    :type cache: dict | bytes

    """
    cache = Cache.from_dict(cache)
    return web.Response(status=200)


async def caches_upgrade_firmware(request: web.Request, resource_group_name, api_version, subscription_id, cache_name) -> web.Response:
    """caches_upgrade_firmware

    Upgrade a Cache&#39;s firmware if a new version is available. Otherwise, this operation has no effect.

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
