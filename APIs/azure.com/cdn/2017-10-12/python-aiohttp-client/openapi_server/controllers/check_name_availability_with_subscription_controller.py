from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def check_name_availability_with_subscription(request: web.Request, subscription_id, api_version, check_name_availability_input) -> web.Response:
    """check_name_availability_with_subscription

    Check the availability of a resource name. This is needed for resources where name is globally unique, such as a CDN endpoint.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param check_name_availability_input: Input to check.
    :type check_name_availability_input: dict | bytes

    """
    check_name_availability_input = CheckNameAvailabilityInput.from_dict(check_name_availability_input)
    return web.Response(status=200)
