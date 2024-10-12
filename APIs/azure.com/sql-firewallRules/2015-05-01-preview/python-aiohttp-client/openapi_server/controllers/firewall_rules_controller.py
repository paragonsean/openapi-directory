from typing import List, Dict
from aiohttp import web

from openapi_server.models.firewall_rule import FirewallRule
from openapi_server.models.firewall_rule_list import FirewallRuleList
from openapi_server.models.firewall_rule_list_result import FirewallRuleListResult
from openapi_server import util


async def firewall_rules_create_or_update(request: web.Request, resource_group_name, server_name, firewall_rule_name, subscription_id, api_version, parameters) -> web.Response:
    """firewall_rules_create_or_update

    Creates or updates a firewall rule.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param firewall_rule_name: The name of the firewall rule.
    :type firewall_rule_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The required parameters for creating or updating a firewall rule.
    :type parameters: dict | bytes

    """
    parameters = FirewallRule.from_dict(parameters)
    return web.Response(status=200)


async def firewall_rules_delete(request: web.Request, resource_group_name, server_name, firewall_rule_name, subscription_id, api_version) -> web.Response:
    """firewall_rules_delete

    Deletes a firewall rule.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param firewall_rule_name: The name of the firewall rule.
    :type firewall_rule_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def firewall_rules_get(request: web.Request, resource_group_name, server_name, firewall_rule_name, subscription_id, api_version) -> web.Response:
    """firewall_rules_get

    Gets a firewall rule.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param firewall_rule_name: The name of the firewall rule.
    :type firewall_rule_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def firewall_rules_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """firewall_rules_list_by_server

    Gets a list of firewall rules.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def firewall_rules_replace(request: web.Request, resource_group_name, server_name, subscription_id, api_version, parameters) -> web.Response:
    """firewall_rules_replace

    Replaces all firewall rules on the server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = FirewallRuleList.from_dict(parameters)
    return web.Response(status=200)
