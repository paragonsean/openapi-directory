from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server import util


async def event_hub_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, eventhub_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """event_hub_get_authorization_rule

    Returns the specified authorization rule.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param eventhub_name: The eventhub name.
    :type eventhub_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def event_hub_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, eventhub_name, api_version, subscription_id) -> web.Response:
    """event_hub_list_authorization_rules

    Gets authorization rules for a eventhub.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param eventhub_name: The eventhub name.
    :type eventhub_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
