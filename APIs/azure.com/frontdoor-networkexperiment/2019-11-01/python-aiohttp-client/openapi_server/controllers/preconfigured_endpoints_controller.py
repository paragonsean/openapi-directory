from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.preconfigured_endpoint_list import PreconfiguredEndpointList
from openapi_server import util


async def preconfigured_endpoints_list(request: web.Request, subscription_id, api_version, resource_group_name, profile_name) -> web.Response:
    """Gets a list of Preconfigured Endpoints

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str

    """
    return web.Response(status=200)
