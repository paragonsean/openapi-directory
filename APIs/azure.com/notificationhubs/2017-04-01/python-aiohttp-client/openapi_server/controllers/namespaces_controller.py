from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_availability_parameters import CheckAvailabilityParameters
from openapi_server.models.check_availability_result import CheckAvailabilityResult
from openapi_server.models.namespace_create_or_update_parameters import NamespaceCreateOrUpdateParameters
from openapi_server.models.namespace_list_result import NamespaceListResult
from openapi_server.models.namespace_patch_parameters import NamespacePatchParameters
from openapi_server.models.namespace_resource import NamespaceResource
from openapi_server.models.policykey_resource import PolicykeyResource
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server import util


async def namespaces_check_availability(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_check_availability

    Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The namespace name.
    :type parameters: dict | bytes

    """
    parameters = CheckAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update

    Creates/Updates a service namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create a Namespace Resource.
    :type parameters: dict | bytes

    """
    parameters = NamespaceCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_create_or_update_authorization_rule

    Creates an authorization rule for a namespace

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param authorization_rule_name: Authorization Rule Name.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The shared access authorization rule.
    :type parameters: dict | bytes

    """
    parameters = SharedAccessAuthorizationRuleCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_delete(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete

    Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_delete_authorization_rule

    Deletes a namespace authorization rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param authorization_rule_name: Authorization Rule Name.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_get

    Returns the description for the specified namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_get_authorization_rule

    Gets an authorization rule for a namespace by name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param authorization_rule_name: Authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """namespaces_list

    Lists the available namespaces within a resourceGroup.

    :param resource_group_name: The name of the resource group. If resourceGroupName value is null the method lists all the namespaces within subscription
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """namespaces_list_all

    Lists all the available namespaces within the subscription irrespective of the resourceGroups.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_authorization_rules

    Gets the authorization rules for a namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_list_keys(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """namespaces_list_keys

    Gets the Primary and Secondary ConnectionStrings to the namespace 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param authorization_rule_name: The connection string of the namespace for the specified authorizationRule.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def namespaces_patch(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_patch

    Patches the existing namespace

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to patch a Namespace Resource.
    :type parameters: dict | bytes

    """
    parameters = NamespacePatchParameters.from_dict(parameters)
    return web.Response(status=200)


async def namespaces_regenerate_keys(request: web.Request, resource_group_name, namespace_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """namespaces_regenerate_keys

    Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param authorization_rule_name: The connection string of the namespace for the specified authorizationRule.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to regenerate the Namespace Authorization Rule Key.
    :type parameters: dict | bytes

    """
    parameters = PolicykeyResource.from_dict(parameters)
    return web.Response(status=200)
