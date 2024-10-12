from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_location import FabricLocation
from openapi_server.models.fabric_location_list import FabricLocationList
from openapi_server import util


async def fabric_locations_get(request: web.Request, subscription_id, resource_group_name, fabric_location, api_version) -> web.Response:
    """fabric_locations_get

    Returns the requested fabric location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param fabric_location: Fabric location.
    :type fabric_location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def fabric_locations_list(request: web.Request, subscription_id, resource_group_name, api_version, filter=None) -> web.Response:
    """fabric_locations_list

    Returns a list of all fabric locations.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
