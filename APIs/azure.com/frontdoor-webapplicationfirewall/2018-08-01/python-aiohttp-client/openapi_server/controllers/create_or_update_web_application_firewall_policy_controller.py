from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.web_application_firewall_policy import WebApplicationFirewallPolicy
from openapi_server import util


async def policies_create_or_update(request: web.Request, resource_group_name, policy_name, subscription_id, api_version, parameters) -> web.Response:
    """policies_create_or_update

    Creates or update policy with specified rule set name within a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param policy_name: The name of the resource group.
    :type policy_name: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: Policy to be created.
    :type parameters: dict | bytes

    """
    parameters = WebApplicationFirewallPolicy.from_dict(parameters)
    return web.Response(status=200)
