from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server import util


async def storage_sync_services_check_name_availability(request: web.Request, location_name, api_version, subscription_id, parameters) -> web.Response:
    """storage_sync_services_check_name_availability

    Check the give namespace name availability.

    :param location_name: The desired region for the name check.
    :type location_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters to check availability of the given namespace name
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)
