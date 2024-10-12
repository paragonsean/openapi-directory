from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_lake_store_account import DataLakeStoreAccount
from openapi_server.models.data_lake_store_account_list_result import DataLakeStoreAccountListResult
from openapi_server.models.data_lake_store_firewall_rule_list_result import DataLakeStoreFirewallRuleListResult
from openapi_server.models.firewall_rule import FirewallRule
from openapi_server import util


async def account_create(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """account_create

    Creates the specified Data Lake Store account.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param name: The name of the Data Lake Store account to create.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create the Data Lake Store account.
    :type parameters: dict | bytes

    """
    parameters = DataLakeStoreAccount.from_dict(parameters)
    return web.Response(status=200)


async def account_create_or_update_firewall_rule(request: web.Request, resource_group_name, account_name, name, api_version, subscription_id, parameters) -> web.Response:
    """account_create_or_update_firewall_rule

    Creates or updates the specified firewall rule.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account to which to add the firewall rule.
    :type account_name: str
    :param name: The name of the firewall rule to create or update.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create the create firewall rule.
    :type parameters: dict | bytes

    """
    parameters = FirewallRule.from_dict(parameters)
    return web.Response(status=200)


async def account_delete(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """account_delete

    Deletes the specified Data Lake Store account.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account to delete.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def account_delete_firewall_rule(request: web.Request, resource_group_name, account_name, firewall_rule_name, api_version, subscription_id) -> web.Response:
    """account_delete_firewall_rule

    Deletes the specified firewall rule from the specified Data Lake Store account

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account from which to delete the firewall rule.
    :type account_name: str
    :param firewall_rule_name: The name of the firewall rule to delete.
    :type firewall_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def account_enable_key_vault(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """account_enable_key_vault

    Attempts to enable a user managed key vault for encryption of the specified Data Lake Store account.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account to attempt to enable the Key Vault for.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def account_get(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """account_get

    Gets the specified Data Lake Store account.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account to retrieve.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def account_get_firewall_rule(request: web.Request, resource_group_name, account_name, firewall_rule_name, api_version, subscription_id) -> web.Response:
    """account_get_firewall_rule

    Gets the specified Data Lake Store firewall rule.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account from which to get the firewall rule.
    :type account_name: str
    :param firewall_rule_name: The name of the firewall rule to retrieve.
    :type firewall_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def account_list(request: web.Request, api_version, subscription_id, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None, search=None, format=None) -> web.Response:
    """account_list

    Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories/$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool
    :param search: A free form search. A free-text search expression to match for whether a particular entry should be included in the feed, e.g. Categories?$search&#x3D;blue OR green. Optional.
    :type search: str
    :param format: The desired return format. Return the response in particular format without access to request headers for standard content-type negotiation (e.g Orders?$format&#x3D;json). Optional.
    :type format: str

    """
    return web.Response(status=200)


async def account_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None, search=None, format=None) -> web.Response:
    """account_list_by_resource_group

    Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account(s).
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories/$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: A Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool
    :param search: A free form search. A free-text search expression to match for whether a particular entry should be included in the feed, e.g. Categories?$search&#x3D;blue OR green. Optional.
    :type search: str
    :param format: The desired return format. Return the response in particular format without access to request headers for standard content-type negotiation (e.g Orders?$format&#x3D;json). Optional.
    :type format: str

    """
    return web.Response(status=200)


async def account_list_firewall_rules(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """account_list_firewall_rules

    Lists the Data Lake Store firewall rules within the specified Data Lake Store account.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account from which to get the firewall rules.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def account_update(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """account_update

    Updates the specified Data Lake Store account information.

    :param resource_group_name: The name of the Azure resource group that contains the Data Lake Store account.
    :type resource_group_name: str
    :param name: The name of the Data Lake Store account to update.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update the Data Lake Store account.
    :type parameters: dict | bytes

    """
    parameters = DataLakeStoreAccount.from_dict(parameters)
    return web.Response(status=200)
