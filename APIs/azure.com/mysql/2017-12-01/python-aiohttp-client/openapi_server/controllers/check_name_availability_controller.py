from typing import List, Dict
from aiohttp import web

from openapi_server.models.name_availability import NameAvailability
from openapi_server.models.name_availability_request import NameAvailabilityRequest
from openapi_server import util


async def check_name_availability_execute(request: web.Request, api_version, subscription_id, name_availability_request) -> web.Response:
    """check_name_availability_execute

    Check the availability of name for resource

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param name_availability_request: The required parameters for checking if resource name is available.
    :type name_availability_request: dict | bytes

    """
    name_availability_request = NameAvailabilityRequest.from_dict(name_availability_request)
    return web.Response(status=200)
