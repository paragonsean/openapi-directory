from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_service_check_name_availability_parameters import DeviceServiceCheckNameAvailabilityParameters
from openapi_server.models.device_service_name_availability_info import DeviceServiceNameAvailabilityInfo
from openapi_server.models.error_details import ErrorDetails
from openapi_server import util


async def services_check_device_service_name_availability(request: web.Request, api_version, subscription_id, device_service_check_name_availability_parameters) -> web.Response:
    """services_check_device_service_name_availability

    Check if a Windows IoT Device Service name is available.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param device_service_check_name_availability_parameters: Set the name parameter in the DeviceServiceCheckNameAvailabilityParameters structure to the name of the Windows IoT Device Service to check.
    :type device_service_check_name_availability_parameters: dict | bytes

    """
    device_service_check_name_availability_parameters = DeviceServiceCheckNameAvailabilityParameters.from_dict(device_service_check_name_availability_parameters)
    return web.Response(status=200)
