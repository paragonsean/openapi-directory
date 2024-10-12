from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_rule_resource import AlertRuleResource
from openapi_server.models.alert_rule_resource_collection import AlertRuleResourceCollection
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def alert_rules_create_or_update(request: web.Request, resource_group_name, rule_name, api_version, subscription_id, parameters) -> web.Response:
    """alert_rules_create_or_update

    Creates or updates an alert rule.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param parameters: The parameters of the rule to create or update.
    :type parameters: dict | bytes

    """
    parameters = AlertRuleResource.from_dict(parameters)
    return web.Response(status=200)


async def alert_rules_delete(request: web.Request, resource_group_name, rule_name, api_version, subscription_id) -> web.Response:
    """alert_rules_delete

    Deletes an alert rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def alert_rules_get(request: web.Request, resource_group_name, rule_name, api_version, subscription_id) -> web.Response:
    """alert_rules_get

    Gets an alert rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def alert_rules_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """alert_rules_list_by_resource_group

    List the alert rules within a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def alert_rules_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """alert_rules_list_by_subscription

    List the alert rules within a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
