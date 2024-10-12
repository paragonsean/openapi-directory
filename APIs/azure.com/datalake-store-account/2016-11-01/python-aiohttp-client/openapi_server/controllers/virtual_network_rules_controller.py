from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_virtual_network_rule_parameters import CreateOrUpdateVirtualNetworkRuleParameters
from openapi_server.models.update_virtual_network_rule_parameters import UpdateVirtualNetworkRuleParameters
from openapi_server.models.virtual_network_rule import VirtualNetworkRule
from openapi_server.models.virtual_network_rule_list_result import VirtualNetworkRuleListResult
from openapi_server import util


async def virtual_network_rules_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, virtual_network_rule_name, api_version, parameters) -> web.Response:
    """virtual_network_rules_create_or_update

    Creates or updates the specified virtual network rule. During update, the virtual network rule with the specified name will be replaced with this new virtual network rule.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param virtual_network_rule_name: The name of the virtual network rule to create or update.
    :type virtual_network_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to create or update the virtual network rule.
    :type parameters: dict | bytes

    """
    parameters = CreateOrUpdateVirtualNetworkRuleParameters.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_rules_delete(request: web.Request, subscription_id, resource_group_name, account_name, virtual_network_rule_name, api_version) -> web.Response:
    """virtual_network_rules_delete

    Deletes the specified virtual network rule from the specified Data Lake Store account.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param virtual_network_rule_name: The name of the virtual network rule to delete.
    :type virtual_network_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_network_rules_get(request: web.Request, subscription_id, resource_group_name, account_name, virtual_network_rule_name, api_version) -> web.Response:
    """virtual_network_rules_get

    Gets the specified Data Lake Store virtual network rule.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param virtual_network_rule_name: The name of the virtual network rule to retrieve.
    :type virtual_network_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_network_rules_list_by_account(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """virtual_network_rules_list_by_account

    Lists the Data Lake Store virtual network rules within the specified Data Lake Store account.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_network_rules_update(request: web.Request, subscription_id, resource_group_name, account_name, virtual_network_rule_name, api_version, parameters=None) -> web.Response:
    """virtual_network_rules_update

    Updates the specified virtual network rule.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param virtual_network_rule_name: The name of the virtual network rule to update.
    :type virtual_network_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to update the virtual network rule.
    :type parameters: dict | bytes

    """
    parameters = UpdateVirtualNetworkRuleParameters.from_dict(parameters)
    return web.Response(status=200)
