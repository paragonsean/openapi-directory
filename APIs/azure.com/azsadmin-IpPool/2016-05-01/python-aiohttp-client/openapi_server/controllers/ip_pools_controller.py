from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_pool import IpPool
from openapi_server.models.ip_pool_list import IpPoolList
from openapi_server import util


async def ip_pools_create_or_update(request: web.Request, subscription_id, resource_group_name, location, ip_pool, api_version, pool) -> web.Response:
    """ip_pools_create_or_update

    Create an IP pool.  Once created an IP pool cannot be deleted.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param ip_pool: IP pool name.
    :type ip_pool: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool: IP pool object to send.
    :type pool: dict | bytes

    """
    pool = IpPool.from_dict(pool)
    return web.Response(status=200)


async def ip_pools_get(request: web.Request, subscription_id, resource_group_name, location, ip_pool, api_version) -> web.Response:
    """ip_pools_get

    Return the requested IP pool.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param ip_pool: IP pool name.
    :type ip_pool: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def ip_pools_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """ip_pools_list

    Returns a list of all IP pools at a certain location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
