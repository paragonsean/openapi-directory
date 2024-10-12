from typing import List, Dict
from aiohttp import web

from openapi_server.models.mac_address_pool import MacAddressPool
from openapi_server.models.mac_address_pool_list import MacAddressPoolList
from openapi_server import util


async def mac_address_pools_get(request: web.Request, subscription_id, resource_group_name, location, mac_address_pool, api_version) -> web.Response:
    """mac_address_pools_get

    Returns the requested MAC address pool.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param mac_address_pool: Name of the MAC address pool.
    :type mac_address_pool: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def mac_address_pools_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """mac_address_pools_list

    Returns a list of all MAC address pools at a location.

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
