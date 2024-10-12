from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_request import CheckNameAvailabilityRequest
from openapi_server.models.check_name_availability_response import CheckNameAvailabilityResponse
from openapi_server import util


async def servers_check_name_availability(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """servers_check_name_availability

    Determines whether a resource can be created with the specified name.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param parameters: The parameters to request for name availability.
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityRequest.from_dict(parameters)
    return web.Response(status=200)
