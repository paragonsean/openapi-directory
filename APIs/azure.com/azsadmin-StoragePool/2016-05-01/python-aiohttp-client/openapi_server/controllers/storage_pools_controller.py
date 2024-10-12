from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_pool import StoragePool
from openapi_server.models.storage_pool_list import StoragePoolList
from openapi_server import util


async def storage_pools_get(request: web.Request, subscription_id, resource_group_name, location, storage_sub_system, storage_pool, api_version) -> web.Response:
    """storage_pools_get

    Return the requested a storage pool.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param storage_sub_system: Name of the storage system.
    :type storage_sub_system: str
    :param storage_pool: Storage pool name.
    :type storage_pool: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_pools_list(request: web.Request, subscription_id, resource_group_name, location, storage_sub_system, api_version, filter=None) -> web.Response:
    """storage_pools_list

    Returns a list of all storage pools for a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param storage_sub_system: Name of the storage system.
    :type storage_sub_system: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
