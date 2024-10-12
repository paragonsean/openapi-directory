from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_request import CheckNameRequest
from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def digital_twins_check_name_availability(request: web.Request, api_version, subscription_id, location, digital_twins_instance_check_name) -> web.Response:
    """digital_twins_check_name_availability

    Check if a DigitalTwinsInstance name is available.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param location: Location of DigitalTwinsInstance.
    :type location: str
    :param digital_twins_instance_check_name: Set the name parameter in the DigitalTwinsInstanceCheckName structure to the name of the DigitalTwinsInstance to check.
    :type digital_twins_instance_check_name: dict | bytes

    """
    digital_twins_instance_check_name = CheckNameRequest.from_dict(digital_twins_instance_check_name)
    return web.Response(status=200)
