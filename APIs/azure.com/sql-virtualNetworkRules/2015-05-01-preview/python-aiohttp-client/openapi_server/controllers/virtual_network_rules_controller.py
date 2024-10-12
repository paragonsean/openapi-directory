from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_network_rule import VirtualNetworkRule
from openapi_server.models.virtual_network_rule_list_result import VirtualNetworkRuleListResult
from openapi_server import util


async def virtual_network_rules_create_or_update(request: web.Request, resource_group_name, server_name, virtual_network_rule_name, subscription_id, api_version, parameters) -> web.Response:
    """virtual_network_rules_create_or_update

    Creates or updates an existing virtual network rule.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param virtual_network_rule_name: The name of the virtual network rule.
    :type virtual_network_rule_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested virtual Network Rule Resource state.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkRule.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_rules_delete(request: web.Request, resource_group_name, server_name, virtual_network_rule_name, subscription_id, api_version) -> web.Response:
    """virtual_network_rules_delete

    Deletes the virtual network rule with the given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param virtual_network_rule_name: The name of the virtual network rule.
    :type virtual_network_rule_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_network_rules_get(request: web.Request, resource_group_name, server_name, virtual_network_rule_name, subscription_id, api_version) -> web.Response:
    """virtual_network_rules_get

    Gets a virtual network rule.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param virtual_network_rule_name: The name of the virtual network rule.
    :type virtual_network_rule_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_network_rules_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """virtual_network_rules_list_by_server

    Gets a list of virtual network rules in a server.

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
