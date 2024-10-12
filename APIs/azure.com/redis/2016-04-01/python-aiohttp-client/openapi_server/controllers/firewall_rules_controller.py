from typing import List, Dict
from aiohttp import web

from openapi_server.models.redis_firewall_rule import RedisFirewallRule
from openapi_server.models.redis_firewall_rule_list_result import RedisFirewallRuleListResult
from openapi_server import util


async def firewall_rules_list_0(request: web.Request, api_version, subscription_id, resource_group_name, cache_name) -> web.Response:
    """firewall_rules_list_0

    Gets all firewall rules in the specified redis cache.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str

    """
    return web.Response(status=200)


async def redis_firewall_rule_create_or_update_0(request: web.Request, resource_group_name, cache_name, rule_name, api_version, subscription_id, parameters) -> web.Response:
    """redis_firewall_rule_create_or_update_0

    Create or update a redis cache firewall rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str
    :param rule_name: The name of the firewall rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update redis firewall rule operation.
    :type parameters: dict | bytes

    """
    parameters = RedisFirewallRule.from_dict(parameters)
    return web.Response(status=200)


async def redis_firewall_rule_delete_0(request: web.Request, resource_group_name, cache_name, rule_name, api_version, subscription_id) -> web.Response:
    """redis_firewall_rule_delete_0

    Deletes a single firewall rule in a specified redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str
    :param rule_name: The name of the firewall rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_firewall_rule_get_0(request: web.Request, resource_group_name, cache_name, rule_name, api_version, subscription_id) -> web.Response:
    """redis_firewall_rule_get_0

    Gets a single firewall rule in a specified redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str
    :param rule_name: The name of the firewall rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
