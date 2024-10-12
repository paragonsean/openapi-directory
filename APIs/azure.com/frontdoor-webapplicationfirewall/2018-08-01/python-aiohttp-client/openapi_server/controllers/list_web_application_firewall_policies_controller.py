from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.web_application_firewall_policy_list_result import WebApplicationFirewallPolicyListResult
from openapi_server import util


async def policies_list(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """policies_list

    Lists all of the protection policies within a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
