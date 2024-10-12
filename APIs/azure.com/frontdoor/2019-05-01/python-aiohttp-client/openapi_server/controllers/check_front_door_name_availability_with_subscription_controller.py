from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def check_front_door_name_availability_with_subscription(request: web.Request, subscription_id, api_version, check_front_door_name_availability_input) -> web.Response:
    """check_front_door_name_availability_with_subscription

    Check the availability of a Front Door subdomain.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param check_front_door_name_availability_input: Input to check.
    :type check_front_door_name_availability_input: dict | bytes

    """
    check_front_door_name_availability_input = CheckNameAvailabilityInput.from_dict(check_front_door_name_availability_input)
    return web.Response(status=200)
