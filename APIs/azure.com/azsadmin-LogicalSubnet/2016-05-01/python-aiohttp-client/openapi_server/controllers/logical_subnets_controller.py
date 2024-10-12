from typing import List, Dict
from aiohttp import web

from openapi_server.models.logical_subnet import LogicalSubnet
from openapi_server.models.logical_subnet_list import LogicalSubnetList
from openapi_server import util


async def logical_subnets_get(request: web.Request, subscription_id, resource_group_name, location, logical_network, logical_subnet, api_version) -> web.Response:
    """logical_subnets_get

    Returns the requested logical subnet.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param logical_network: Name of the logical network.
    :type logical_network: str
    :param logical_subnet: Name of the logical subnet.
    :type logical_subnet: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def logical_subnets_list(request: web.Request, subscription_id, resource_group_name, location, logical_network, api_version, filter=None) -> web.Response:
    """logical_subnets_list

    Returns a list of all logical subnets.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param logical_network: Name of the logical network.
    :type logical_network: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
