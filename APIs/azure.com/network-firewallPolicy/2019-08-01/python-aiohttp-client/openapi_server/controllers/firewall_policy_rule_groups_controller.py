from typing import List, Dict
from aiohttp import web

from openapi_server.models.firewall_policy_rule_group import FirewallPolicyRuleGroup
from openapi_server.models.firewall_policy_rule_group_list_result import FirewallPolicyRuleGroupListResult
from openapi_server import util


async def firewall_policy_rule_groups_create_or_update(request: web.Request, resource_group_name, firewall_policy_name, rule_group_name, api_version, subscription_id, parameters) -> web.Response:
    """firewall_policy_rule_groups_create_or_update

    Creates or updates the specified FirewallPolicyRuleGroup.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy.
    :type firewall_policy_name: str
    :param rule_group_name: The name of the FirewallPolicyRuleGroup.
    :type rule_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update FirewallPolicyRuleGroup operation.
    :type parameters: dict | bytes

    """
    parameters = FirewallPolicyRuleGroup.from_dict(parameters)
    return web.Response(status=200)


async def firewall_policy_rule_groups_delete(request: web.Request, resource_group_name, firewall_policy_name, rule_group_name, api_version, subscription_id) -> web.Response:
    """firewall_policy_rule_groups_delete

    Deletes the specified FirewallPolicyRuleGroup.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy.
    :type firewall_policy_name: str
    :param rule_group_name: The name of the FirewallPolicyRuleGroup.
    :type rule_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def firewall_policy_rule_groups_get(request: web.Request, resource_group_name, firewall_policy_name, rule_group_name, api_version, subscription_id) -> web.Response:
    """firewall_policy_rule_groups_get

    Gets the specified FirewallPolicyRuleGroup.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param firewall_policy_name: The name of the Firewall Policy.
    :type firewall_policy_name: str
    :param rule_group_name: The name of the FirewallPolicyRuleGroup.
    :type rule_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def firewall_policy_rule_groups_list(request: web.Request, resource_group_name, firewall_policy_name, api_version, subscription_id) -> web.Response:
    """firewall_policy_rule_groups_list

    Lists all FirewallPolicyRuleGroups in a FirewallPolicy resource.

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
