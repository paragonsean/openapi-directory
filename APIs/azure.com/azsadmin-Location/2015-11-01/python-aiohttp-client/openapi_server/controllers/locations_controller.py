from typing import List, Dict
from aiohttp import web

from openapi_server.models.location import Location
from openapi_server.models.location_list import LocationList
from openapi_server.models.operations_status import OperationsStatus
from openapi_server import util


async def locations_create_or_update(request: web.Request, subscription_id, location, api_version, new_location) -> web.Response:
    """locations_create_or_update

    Updates the specified location.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The AzureStack location.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param new_location: The new location
    :type new_location: dict | bytes

    """
    new_location = Location.from_dict(new_location)
    return web.Response(status=200)


async def locations_get(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """locations_get

    Get the specified location.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The AzureStack location.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def locations_get_operations_status(request: web.Request, subscription_id, location, operations_status_name, api_version) -> web.Response:
    """locations_get_operations_status

    Get the operation status.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The AzureStack location.
    :type location: str
    :param operations_status_name: The operation status name.
    :type operations_status_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def locations_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """locations_list

    Get a list of all AzureStack location.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
