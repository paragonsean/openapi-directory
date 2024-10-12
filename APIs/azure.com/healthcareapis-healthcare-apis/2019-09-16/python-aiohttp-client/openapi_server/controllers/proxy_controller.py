from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.services_name_availability_info import ServicesNameAvailabilityInfo
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available Healthcare service REST API operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_check_name_availability(request: web.Request, api_version, subscription_id, check_name_availability_inputs) -> web.Response:
    """services_check_name_availability

    Check if a service instance name is available.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param check_name_availability_inputs: Set the name parameter in the CheckNameAvailabilityParameters structure to the name of the service instance to check.
    :type check_name_availability_inputs: dict | bytes

    """
    check_name_availability_inputs = CheckNameAvailabilityParameters.from_dict(check_name_availability_inputs)
    return web.Response(status=200)
