from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_firewall_rule_parameters import CreateOrUpdateFirewallRuleParameters
from openapi_server.models.firewall_rule import FirewallRule
from openapi_server.models.firewall_rule_list_result import FirewallRuleListResult
from openapi_server.models.update_firewall_rule_parameters import UpdateFirewallRuleParameters
from openapi_server import util


async def firewall_rules_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, firewall_rule_name, api_version, parameters) -> web.Response:
    """firewall_rules_create_or_update

    Creates or updates the specified firewall rule. During update, the firewall rule with the specified name will be replaced with this new firewall rule.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param firewall_rule_name: The name of the firewall rule to create or update.
    :type firewall_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to create or update the firewall rule.
    :type parameters: dict | bytes

    """
    parameters = CreateOrUpdateFirewallRuleParameters.from_dict(parameters)
    return web.Response(status=200)


async def firewall_rules_delete(request: web.Request, subscription_id, resource_group_name, account_name, firewall_rule_name, api_version) -> web.Response:
    """firewall_rules_delete

    Deletes the specified firewall rule from the specified Data Lake Store account.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param firewall_rule_name: The name of the firewall rule to delete.
    :type firewall_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def firewall_rules_get(request: web.Request, subscription_id, resource_group_name, account_name, firewall_rule_name, api_version) -> web.Response:
    """firewall_rules_get

    Gets the specified Data Lake Store firewall rule.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param firewall_rule_name: The name of the firewall rule to retrieve.
    :type firewall_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def firewall_rules_list_by_account(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """firewall_rules_list_by_account

    Lists the Data Lake Store firewall rules within the specified Data Lake Store account.

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


async def firewall_rules_update(request: web.Request, subscription_id, resource_group_name, account_name, firewall_rule_name, api_version, parameters=None) -> web.Response:
    """firewall_rules_update

    Updates the specified firewall rule.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param firewall_rule_name: The name of the firewall rule to update.
    :type firewall_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to update the firewall rule.
    :type parameters: dict | bytes

    """
    parameters = UpdateFirewallRuleParameters.from_dict(parameters)
    return web.Response(status=200)
