from typing import List, Dict
from aiohttp import web

from openapi_server.models.edge_gateway_pool import EdgeGatewayPool
from openapi_server.models.edge_gateway_pool_list import EdgeGatewayPoolList
from openapi_server import util


async def edge_gateway_pools_get(request: web.Request, subscription_id, resource_group_name, location, edge_gateway_pool, api_version) -> web.Response:
    """edge_gateway_pools_get

    Returns the requested edge gateway pool object.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param edge_gateway_pool: Name of the edge gateway pool.
    :type edge_gateway_pool: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def edge_gateway_pools_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """edge_gateway_pools_list

    Returns a list of all edge gateway pool objects at a location.

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
