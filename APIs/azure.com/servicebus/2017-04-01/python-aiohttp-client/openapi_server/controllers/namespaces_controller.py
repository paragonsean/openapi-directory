from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_keys import AccessKeys
from openapi_server.models.check_name_availability import CheckNameAvailability
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.network_rule_set import NetworkRuleSet
from openapi_server.models.network_rule_set_list_result import NetworkRuleSetListResult
from openapi_server.models.regenerate_access_key_parameters import RegenerateAccessKeyParameters
from openapi_server.models.sb_authorization_rule import SBAuthorizationRule
from openapi_server.models.sb_authorization_rule_list_result import SBAuthorizationRuleListResult
from openapi_server.models.sb_namespace import SBNamespace
from openapi_server.models.sb_namespace_list_result import SBNamespaceListResult
from openapi_server.models.sb_namespace_migrate import SBNamespaceMigrate
from openapi_server.models.sb_namespace_update_parameters import SBNamespaceUpdateParameters
from openapi_server import util


async def namespaces_check_name_availability(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_check_name_availability

    Check the give namespace name availability.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to check availability of the given namespace name
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailability.from_dict(parameters)
    return web.Response(status=200)


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


async def namespaces_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_authorization_rule

    Creates or updates an authorization rule for a namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The shared access authorization rule.
    :type parameters: dict | bytes

    """
    parameters = SBAuthorizationRule.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update_network_rule_set(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_network_rule_set

    Create or update NetworkRuleSet for a Namespace.

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


async def namespaces_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete_authorization_rule

    Deletes a namespace authorization rule.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
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


async def namespaces_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_get_authorization_rule

    Gets an authorization rule for a namespace by rule name.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
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


async def namespaces_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """namespaces_list

    Gets all the available namespaces within the subscription, irrespective of the resource groups.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_authorization_rules

    Gets the authorization rules for a namespace.

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


async def namespaces_list_keys(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_keys

    Gets the primary and secondary connection strings for the namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_network_rule_sets(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_network_rule_sets

    Gets list of NetworkRuleSet for a Namespace.

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


async def namespaces_migrate(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_migrate

    This operation Migrate the given namespace to provided name type

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to migrate namespace type.
    :type parameters: dict | bytes

    """
    parameters = SBNamespaceMigrate.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_regenerate_keys(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_regenerate_keys

    Regenerates the primary or secondary connection strings for the namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to regenerate the authorization rule.
    :type parameters: dict | bytes

    """
    parameters = RegenerateAccessKeyParameters.from_dict(parameters)
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
