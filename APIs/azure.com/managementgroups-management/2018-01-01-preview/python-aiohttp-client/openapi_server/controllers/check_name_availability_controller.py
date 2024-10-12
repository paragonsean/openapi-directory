from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_request import CheckNameAvailabilityRequest
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def check_name_availability(request: web.Request, api_version, check_name_availability_request) -> web.Response:
    """check_name_availability

    Checks if the specified management group name is valid and unique

    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str
    :param check_name_availability_request: Management group name availability check parameters.
    :type check_name_availability_request: dict | bytes

    """
    check_name_availability_request = CheckNameAvailabilityRequest.from_dict(check_name_availability_request)
    return web.Response(status=200)
