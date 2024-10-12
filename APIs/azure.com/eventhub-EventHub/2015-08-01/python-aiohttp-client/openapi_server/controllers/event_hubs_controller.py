from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_hub_create_or_update_parameters import EventHubCreateOrUpdateParameters
from openapi_server.models.event_hub_list_result import EventHubListResult
from openapi_server.models.event_hub_resource import EventHubResource
from openapi_server.models.regenerate_keys_parameters import RegenerateKeysParameters
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server import util


async def event_hubs_create_or_update(request: web.Request, resource_group_name, namespace_name, event_hub_name, api_version, subscription_id, parameters) -> web.Response:
    """event_hubs_create_or_update

    Creates or updates a new Event Hub as a nested resource within a Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create an Event Hub resource.
    :type parameters: dict | bytes

    """
    parameters = EventHubCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def event_hubs_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, event_hub_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """event_hubs_create_or_update_authorization_rule

    Creates or updates an AuthorizationRule for the specified Event Hub.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
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


async def event_hubs_delete(request: web.Request, resource_group_name, namespace_name, event_hub_name, api_version, subscription_id) -> web.Response:
    """event_hubs_delete

    Deletes an Event Hub from the specified Namespace and resource group.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, event_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """event_hubs_delete_authorization_rule

    Deletes an Event Hub AuthorizationRule.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_get(request: web.Request, resource_group_name, namespace_name, event_hub_name, api_version, subscription_id) -> web.Response:
    """event_hubs_get

    Gets an Event Hubs description for the specified Event Hub.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, event_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """event_hubs_get_authorization_rule

    Gets an AuthorizationRule for an Event Hub by rule name.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_list_all(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """event_hubs_list_all

    Gets all the Event Hubs in a Namespace.

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


async def event_hubs_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, event_hub_name, api_version, subscription_id) -> web.Response:
    """event_hubs_list_authorization_rules

    Gets the authorization rules for an Event Hub.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_list_keys(request: web.Request, resource_group_name, namespace_name, event_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """event_hubs_list_keys

    Gets the ACS and SAS connection strings for the Event Hub.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_post_authorization_rule(request: web.Request, resource_group_name, namespace_name, event_hub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """event_hubs_post_authorization_rule

    Gets an AuthorizationRule for an Event Hub by rule name.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hubs_regenerate_keys(request: web.Request, resource_group_name, namespace_name, event_hub_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """event_hubs_regenerate_keys

    Regenerates the ACS and SAS connection strings for the Event Hub.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to regenerate the AuthorizationRule Keys (PrimaryKey/SecondaryKey).
    :type parameters: dict | bytes

    """
    parameters = RegenerateKeysParameters.from_dict(parameters)
    return web.Response(status=200)
