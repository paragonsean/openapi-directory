from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_endpoint_policy_list_result import ServiceEndpointPolicyListResult
from openapi_server import util


async def service_endpoint_policies_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """service_endpoint_policies_list_by_resource_group

    Gets all service endpoint Policies in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
