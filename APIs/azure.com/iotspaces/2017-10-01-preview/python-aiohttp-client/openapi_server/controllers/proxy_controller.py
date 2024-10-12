from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.io_t_spaces_name_availability_info import IoTSpacesNameAvailabilityInfo
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def io_t_spaces_check_name_availability(request: web.Request, api_version, subscription_id, operation_inputs) -> web.Response:
    """io_t_spaces_check_name_availability

    Check if an IoTSpaces instance name is available.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param operation_inputs: Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check.
    :type operation_inputs: dict | bytes

    """
    operation_inputs = OperationInputs.from_dict(operation_inputs)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available IoTSpaces service REST API operations.

    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)
