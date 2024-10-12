from typing import List, Dict
from aiohttp import web

from openapi_server.models.region_health import RegionHealth
from openapi_server.models.region_health_list import RegionHealthList
from openapi_server import util


async def region_healths_get(request: web.Request, subscription_id, resource_group_name, location, api_version) -> web.Response:
    """region_healths_get

    Returns the requested health status of a region.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param location: Name of the region
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def region_healths_list(request: web.Request, subscription_id, resource_group_name, api_version, filter=None) -> web.Response:
    """region_healths_list

    Returns the list of all health status for the region.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
