from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_services_list_result import EndpointServicesListResult
from openapi_server import util


async def available_endpoint_services_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """available_endpoint_services_list

    List what values of endpoint services are available for use.

    :param location: The location to check available endpoint services.
    :type location: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
