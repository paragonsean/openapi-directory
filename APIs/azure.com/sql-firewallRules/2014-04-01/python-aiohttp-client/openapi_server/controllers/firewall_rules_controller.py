from typing import List, Dict
from aiohttp import web

from openapi_server.models.firewall_rule import FirewallRule
from openapi_server.models.firewall_rule_list_result import FirewallRuleListResult
from openapi_server import util


async def firewall_rules_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, firewall_rule_name, parameters) -> web.Response:
    """firewall_rules_create_or_update

    Creates or updates a firewall rule.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param firewall_rule_name: The name of the firewall rule.
    :type firewall_rule_name: str
    :param parameters: The required parameters for creating or updating a firewall rule.
    :type parameters: dict | bytes

    """
    parameters = FirewallRule.from_dict(parameters)
    return web.Response(status=200)


async def firewall_rules_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name, firewall_rule_name) -> web.Response:
    """firewall_rules_delete

    Deletes a firewall rule.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param firewall_rule_name: The name of the firewall rule.
    :type firewall_rule_name: str

    """
    return web.Response(status=200)


async def firewall_rules_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, firewall_rule_name) -> web.Response:
    """firewall_rules_get

    Gets a firewall rule.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param firewall_rule_name: The name of the firewall rule.
    :type firewall_rule_name: str

    """
    return web.Response(status=200)


async def firewall_rules_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """firewall_rules_list_by_server

    Returns a list of firewall rules.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)
