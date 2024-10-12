from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_name_availability import ResourceNameAvailability
from openapi_server.models.resource_name_availability_request import ResourceNameAvailabilityRequest
from openapi_server import util


async def check_file_path_availability(request: web.Request, subscription_id, location, api_version, body) -> web.Response:
    """Check file path availability

    Check if a file path is available.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: File path availability request.
    :type body: dict | bytes

    """
    body = ResourceNameAvailabilityRequest.from_dict(body)
    return web.Response(status=200)


async def check_name_availability(request: web.Request, subscription_id, location, api_version, body) -> web.Response:
    """Check resource name availability

    Check if a resource name is available.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Name availability request.
    :type body: dict | bytes

    """
    body = ResourceNameAvailabilityRequest.from_dict(body)
    return web.Response(status=200)
