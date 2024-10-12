from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_search_rule_resource import LogSearchRuleResource
from openapi_server.models.log_search_rule_resource_collection import LogSearchRuleResourceCollection
from openapi_server.models.log_search_rule_resource_patch import LogSearchRuleResourcePatch
from openapi_server import util


async def scheduled_query_rules_create_or_update(request: web.Request, subscription_id, resource_group_name, rule_name, api_version, parameters) -> web.Response:
    """scheduled_query_rules_create_or_update

    Creates or updates an log search rule.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters of the rule to create or update.
    :type parameters: dict | bytes

    """
    parameters = LogSearchRuleResource.from_dict(parameters)
    return web.Response(status=200)


async def scheduled_query_rules_delete(request: web.Request, resource_group_name, rule_name, api_version, subscription_id) -> web.Response:
    """scheduled_query_rules_delete

    Deletes a Log Search rule

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


async def scheduled_query_rules_get(request: web.Request, resource_group_name, rule_name, api_version, subscription_id) -> web.Response:
    """scheduled_query_rules_get

    Gets an Log Search rule

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


async def scheduled_query_rules_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """scheduled_query_rules_list_by_resource_group

    List the Log Search rules within a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
    :type filter: str

    """
    return web.Response(status=200)


async def scheduled_query_rules_list_by_subscription(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """scheduled_query_rules_list_by_subscription

    List the Log Search rules within a subscription group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
    :type filter: str

    """
    return web.Response(status=200)


async def scheduled_query_rules_update(request: web.Request, subscription_id, resource_group_name, rule_name, api_version, parameters) -> web.Response:
    """scheduled_query_rules_update

    Update log search Rule.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters of the rule to update.
    :type parameters: dict | bytes

    """
    parameters = LogSearchRuleResourcePatch.from_dict(parameters)
    return web.Response(status=200)
