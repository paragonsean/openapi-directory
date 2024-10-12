from typing import List, Dict
from aiohttp import web

from openapi_server.models.capacity_pool import CapacityPool
from openapi_server.models.capacity_pool_list import CapacityPoolList
from openapi_server.models.capacity_pool_patch import CapacityPoolPatch
from openapi_server import util


async def pools_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, api_version, body) -> web.Response:
    """Create or Update the specified capacity pool within the resource group

    Create or Update a capacity pool

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Capacity pool object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = CapacityPool.from_dict(body)
    return web.Response(status=200)


async def pools_delete(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, api_version) -> web.Response:
    """Delete a capacity pool

    Delete the specified capacity pool

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def pools_get(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, api_version) -> web.Response:
    """Describe a Capacity Pool

    Get details of the specified capacity pool

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def pools_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Describe all Capacity Pools

    List all capacity pools in the NetApp Account

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def pools_update(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, api_version, body) -> web.Response:
    """Update a capacity pool

    Patch the specified capacity pool

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Capacity pool object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = CapacityPoolPatch.from_dict(body)
    return web.Response(status=200)
