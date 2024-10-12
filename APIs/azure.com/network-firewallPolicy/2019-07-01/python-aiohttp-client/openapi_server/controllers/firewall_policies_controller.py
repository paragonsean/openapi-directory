from typing import List, Dict
from aiohttp import web

from openapi_server.models.firewall_policies_update_tags_default_response import FirewallPoliciesUpdateTagsDefaultResponse
from openapi_server.models.firewall_policies_update_tags_request import FirewallPoliciesUpdateTagsRequest
from openapi_server.models.firewall_policy import FirewallPolicy
from openapi_server.models.firewall_policy_list_result import FirewallPolicyListResult
from openapi_server import util


async def firewall_policies_create_or_update(request: web.Request, resource_group_name, firewall_policy_name, api_version, subscription_id, parameters) -> web.Response:
    """firewall_policies_create_or_update

    Creates or updates the specified Firewall Policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy.
    :type firewall_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update Firewall Policy operation.
    :type parameters: dict | bytes

    """
    parameters = FirewallPolicy.from_dict(parameters)
    return web.Response(status=200)


async def firewall_policies_delete(request: web.Request, resource_group_name, firewall_policy_name, api_version, subscription_id) -> web.Response:
    """firewall_policies_delete

    Deletes the specified Firewall Policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy.
    :type firewall_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def firewall_policies_get(request: web.Request, resource_group_name, firewall_policy_name, api_version, subscription_id, expand=None) -> web.Response:
    """firewall_policies_get

    Gets the specified Firewall Policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy.
    :type firewall_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def firewall_policies_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """firewall_policies_list

    Lists all Firewall Policies in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def firewall_policies_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """firewall_policies_list_all

    Gets all the Firewall Policies in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def firewall_policies_update_tags(request: web.Request, subscription_id, resource_group_name, firewall_policy_name, api_version, firewall_policy_parameters) -> web.Response:
    """firewall_policies_update_tags

    Updates a Firewall Policy Tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the Firewall Policy.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy being updated.
    :type firewall_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param firewall_policy_parameters: Parameters supplied to Update Firewall Policy tags.
    :type firewall_policy_parameters: dict | bytes

    """
    firewall_policy_parameters = FirewallPoliciesUpdateTagsRequest.from_dict(firewall_policy_parameters)
    return web.Response(status=200)
