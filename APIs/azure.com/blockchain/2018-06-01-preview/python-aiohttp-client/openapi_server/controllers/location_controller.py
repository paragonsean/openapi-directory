from typing import List, Dict
from aiohttp import web

from openapi_server.models.consortium_collection import ConsortiumCollection
from openapi_server.models.name_availability import NameAvailability
from openapi_server.models.name_availability_request import NameAvailabilityRequest
from openapi_server import util


async def locations_check_name_availability(request: web.Request, location_name, api_version, subscription_id, name_availability_request=None) -> web.Response:
    """locations_check_name_availability

    To check whether a resource name is available.

    :param location_name: Location Name.
    :type location_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param name_availability_request: Name availability request payload.
    :type name_availability_request: dict | bytes

    """
    name_availability_request = NameAvailabilityRequest.from_dict(name_availability_request)
    return web.Response(status=200)


async def locations_list_consortiums(request: web.Request, location_name, api_version, subscription_id) -> web.Response:
    """locations_list_consortiums

    Lists the available consortiums for a subscription.

    :param location_name: Location Name.
    :type location_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
