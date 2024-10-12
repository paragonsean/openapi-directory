from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameter import CheckNameAvailabilityParameter
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.namespace_create_or_update_parameters import NamespaceCreateOrUpdateParameters
from openapi_server.models.namespace_list_result import NamespaceListResult
from openapi_server.models.namespace_resource import NamespaceResource
from openapi_server.models.namespace_update_parameter import NamespaceUpdateParameter
from openapi_server.models.regenerate_keys_parameters import RegenerateKeysParameters
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server import util


async def namespaces_check_name_availability(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_check_name_availability

    Check the give Namespace name availability.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to check availability of the given Namespace name
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityParameter.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update

    Creates or updates a namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters for creating a namespace resource.
    :type parameters: dict | bytes

    """
    parameters = NamespaceCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_authorization_rule

    Creates or updates an AuthorizationRule for a Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The shared access AuthorizationRule.
    :type parameters: dict | bytes

    """
    parameters = SharedAccessAuthorizationRuleCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_delete(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete

    Deletes an existing namespace. This operation also removes all associated resources under the namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete_authorization_rule

    Deletes an AuthorizationRule for a Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_get

    Gets the description of the specified namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_get_authorization_rule

    Gets an AuthorizationRule for a Namespace by rule name.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_authorization_rules

    Gets a list of authorization rules for a Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_by_resource_group

    Lists the available Namespaces within a resource group.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """namespaces_list_by_subscription

    Lists all the available Namespaces within a subscription, irrespective of the resource groups.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_keys(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_keys

    Gets the primary and secondary connection strings for the Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_regenerate_keys(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_regenerate_keys

    Regenerates the primary or secondary connection strings for the specified Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters required to regenerate the connection string.
    :type parameters: dict | bytes

    """
    parameters = RegenerateKeysParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_update(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_update

    Creates or updates a namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters for updating a namespace resource.
    :type parameters: dict | bytes

    """
    parameters = NamespaceUpdateParameter.from_dict(parameters)
    return web.Response(status=200)
