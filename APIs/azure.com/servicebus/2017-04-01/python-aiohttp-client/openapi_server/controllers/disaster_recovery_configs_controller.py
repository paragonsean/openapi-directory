from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_keys import AccessKeys
from openapi_server.models.arm_disaster_recovery import ArmDisasterRecovery
from openapi_server.models.arm_disaster_recovery_list_result import ArmDisasterRecoveryListResult
from openapi_server.models.check_name_availability import CheckNameAvailability
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sb_authorization_rule import SBAuthorizationRule
from openapi_server.models.sb_authorization_rule_list_result import SBAuthorizationRuleListResult
from openapi_server import util


async def disaster_recovery_configs_break_pairing(request: web.Request, resource_group_name, namespace_name, alias, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_break_pairing

    This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def disaster_recovery_configs_check_name_availability(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """disaster_recovery_configs_check_name_availability

    Check the give namespace name availability.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to check availability of the given namespace name
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailability.from_dict(parameters)
    return web.Response(status=200)


async def disaster_recovery_configs_create_or_update(request: web.Request, resource_group_name, namespace_name, alias, api_version, subscription_id, parameters) -> web.Response:
    """disaster_recovery_configs_create_or_update

    Creates or updates a new Alias(Disaster Recovery configuration)

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters required to create an Alias(Disaster Recovery configuration)
    :type parameters: dict | bytes

    """
    parameters = ArmDisasterRecovery.from_dict(parameters)
    return web.Response(status=200)


async def disaster_recovery_configs_delete(request: web.Request, resource_group_name, namespace_name, alias, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_delete

    Deletes an Alias(Disaster Recovery configuration)

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def disaster_recovery_configs_fail_over(request: web.Request, resource_group_name, namespace_name, alias, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_fail_over

    Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def disaster_recovery_configs_get(request: web.Request, resource_group_name, namespace_name, alias, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_get

    Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def disaster_recovery_configs_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, alias, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_get_authorization_rule

    Gets an authorization rule for a namespace by rule name.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def disaster_recovery_configs_list(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_list

    Gets all Alias(Disaster Recovery configurations)

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


async def disaster_recovery_configs_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, alias, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_list_authorization_rules

    Gets the authorization rules for a namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def disaster_recovery_configs_list_keys(request: web.Request, resource_group_name, namespace_name, alias, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """disaster_recovery_configs_list_keys

    Gets the primary and secondary connection strings for the namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param alias: The Disaster Recovery configuration name
    :type alias: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
