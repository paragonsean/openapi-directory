from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_availability_parameters import CheckAvailabilityParameters
from openapi_server.models.check_availability_resource import CheckAvailabilityResource
from openapi_server.models.notification_hub_create_or_update_parameters import NotificationHubCreateOrUpdateParameters
from openapi_server.models.notification_hub_list_result import NotificationHubListResult
from openapi_server.models.notification_hub_resource import NotificationHubResource
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server import util


async def notification_hubs_check_availability(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """notification_hubs_check_availability

    Checks the availability of the given notificationHub in a namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The notificationHub name.
    :type parameters: dict | bytes

    """
    parameters = CheckAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)


async def notification_hubs_create_or_update(request: web.Request, resource_group_name, namespace_name, notification_hub_name, api_version, subscription_id, parameters) -> web.Response:
    """notification_hubs_create_or_update

    Creates/Update a NotificationHub in a namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update a NotificationHub Resource.
    :type parameters: dict | bytes

    """
    parameters = NotificationHubCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def notification_hubs_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, notification_hub_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """notification_hubs_create_or_update_authorization_rule

    Creates/Updates an authorization rule for a NotificationHub

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
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


async def notification_hubs_delete(request: web.Request, resource_group_name, namespace_name, notification_hub_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_delete

    Deletes a notification hub associated with a namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_hubs_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, notification_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_delete_authorization_rule

    Deletes a notificationHub authorization rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param authorization_rule_name: Authorization Rule Name.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_hubs_get(request: web.Request, resource_group_name, namespace_name, notification_hub_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_get

    Lists the notification hubs associated with a namespace.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_hubs_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, notification_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_get_authorization_rule

    Gets an authorization rule for a NotificationHub by name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param authorization_rule_name: authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_hubs_get_pns_credentials(request: web.Request, resource_group_name, namespace_name, notification_hub_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_get_pns_credentials

    Lists the PNS Credentials associated with a notification hub .

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_hubs_list(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_list

    Lists the notification hubs associated with a namespace.

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


async def notification_hubs_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, notification_hub_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_list_authorization_rules

    Gets the authorization rules for a NotificationHub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_hubs_list_keys(request: web.Request, resource_group_name, namespace_name, notification_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """notification_hubs_list_keys

    Gets the Primary and Secondary ConnectionStrings to the NotificationHub 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param notification_hub_name: The notification hub name.
    :type notification_hub_name: str
    :param authorization_rule_name: The connection string of the NotificationHub for the specified authorizationRule.
    :type authorization_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
