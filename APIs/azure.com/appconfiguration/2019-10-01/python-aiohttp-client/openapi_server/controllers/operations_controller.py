from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.error import Error
from openapi_server.models.name_availability_status import NameAvailabilityStatus
from openapi_server.models.operation_definition_list_result import OperationDefinitionListResult
from openapi_server import util


async def operations_check_name_availability(request: web.Request, subscription_id, api_version, check_name_availability_parameters) -> web.Response:
    """operations_check_name_availability

    Checks whether the configuration store name is available for use.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param check_name_availability_parameters: The object containing information for the availability request.
    :type check_name_availability_parameters: dict | bytes

    """
    check_name_availability_parameters = CheckNameAvailabilityParameters.from_dict(check_name_availability_parameters)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version, skip_token=None) -> web.Response:
    """operations_list

    Lists the operations available from this provider.

    :param api_version: The client API version.
    :type api_version: str
    :param skip_token: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    :type skip_token: str

    """
    return web.Response(status=200)
