from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_service_provider_availability_input import CheckServiceProviderAvailabilityInput
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def check_service_provider_availability(request: web.Request, subscription_id, api_version, check_service_provider_availability_input) -> web.Response:
    """check_service_provider_availability

    Checks if the peering service provider is present within 1000 miles of customer&#39;s location

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param check_service_provider_availability_input: The CheckServiceProviderAvailabilityInput              indicating customer location and service provider.
    :type check_service_provider_availability_input: dict | bytes

    """
    check_service_provider_availability_input = CheckServiceProviderAvailabilityInput.from_dict(check_service_provider_availability_input)
    return web.Response(status=200)
