from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def check_front_door_name_availability(request: web.Request, api_version, check_front_door_name_availability_input) -> web.Response:
    """check_front_door_name_availability

    Check the availability of a Front Door resource name.

    :param api_version: Client API version.
    :type api_version: str
    :param check_front_door_name_availability_input: Input to check.
    :type check_front_door_name_availability_input: dict | bytes

    """
    check_front_door_name_availability_input = CheckNameAvailabilityInput.from_dict(check_front_door_name_availability_input)
    return web.Response(status=200)
