from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.ip_filter_rule import IpFilterRule
from openapi_server.models.ip_filter_rule_list_result import IpFilterRuleListResult
from openapi_server.models.network_rule_set import NetworkRuleSet
from openapi_server.models.sb_namespace import SBNamespace
from openapi_server.models.sb_namespace_list_result import SBNamespaceListResult
from openapi_server.models.sb_namespace_update_parameters import SBNamespaceUpdateParameters
from openapi_server.models.virtual_network_rule import VirtualNetworkRule
from openapi_server.models.virtual_network_rule_list_result import VirtualNetworkRuleListResult
from openapi_server import util


async def namespaces_create_or_update(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update

    Creates or updates a service namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create a namespace resource.
    :type parameters: dict | bytes

    """
    parameters = SBNamespace.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update_ip_filter_rule(request: web.Request, resource_group_name, namespace_name, ip_filter_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_ip_filter_rule

    Creates or updates an IpFilterRule for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param ip_filter_rule_name: The IP Filter Rule name.
    :type ip_filter_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Namespace IpFilterRule.
    :type parameters: dict | bytes

    """
    parameters = IpFilterRule.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update_network_rule_set(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_network_rule_set

    Gets NetworkRuleSet for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Namespace IpFilterRule.
    :type parameters: dict | bytes

    """
    parameters = NetworkRuleSet.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update_virtual_network_rule(request: web.Request, resource_group_name, namespace_name, virtual_network_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_virtual_network_rule

    Creates or updates an VirtualNetworkRule for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param virtual_network_rule_name: The Virtual Network Rule name.
    :type virtual_network_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Namespace VirtualNetworkRule.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkRule.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_delete(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete

    Deletes an existing namespace. This operation also removes all associated resources under the namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_delete_ip_filter_rule(request: web.Request, resource_group_name, namespace_name, ip_filter_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete_ip_filter_rule

    Deletes an IpFilterRule for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param ip_filter_rule_name: The IP Filter Rule name.
    :type ip_filter_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_delete_virtual_network_rule(request: web.Request, resource_group_name, namespace_name, virtual_network_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete_virtual_network_rule

    Deletes an VirtualNetworkRule for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param virtual_network_rule_name: The Virtual Network Rule name.
    :type virtual_network_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_get

    Gets a description for the specified namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get_ip_filter_rule(request: web.Request, resource_group_name, namespace_name, ip_filter_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_get_ip_filter_rule

    Gets an IpFilterRule for a Namespace by rule name.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param ip_filter_rule_name: The IP Filter Rule name.
    :type ip_filter_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get_network_rule_set(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_get_network_rule_set

    Gets NetworkRuleSet for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get_virtual_network_rule(request: web.Request, resource_group_name, namespace_name, virtual_network_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_get_virtual_network_rule

    Gets an VirtualNetworkRule for a Namespace by rule name.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param virtual_network_rule_name: The Virtual Network Rule name.
    :type virtual_network_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """namespaces_list

    Gets all the available namespaces within the subscription, irrespective of the resource groups.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_by_resource_group

    Gets the available namespaces within a resource group.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_ip_filter_rules(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_ip_filter_rules

    Gets a list of IP Filter rules for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_virtual_network_rules(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_virtual_network_rules

    Gets a list of VirtualNetwork rules for a Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_update(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_update

    Updates a service namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update a namespace resource.
    :type parameters: dict | bytes

    """
    parameters = SBNamespaceUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
