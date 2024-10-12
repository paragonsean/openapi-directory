from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_location import UpdateLocation
from openapi_server.models.update_location_list import UpdateLocationList
from openapi_server import util


async def update_locations_get(request: web.Request, subscription_id, resource_group_name, update_location, api_version) -> web.Response:
    """update_locations_get

    Get an update location based on name.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param update_location: The name of the update location.
    :type update_location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def update_locations_list(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """update_locations_list

    Get the list of update locations.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
