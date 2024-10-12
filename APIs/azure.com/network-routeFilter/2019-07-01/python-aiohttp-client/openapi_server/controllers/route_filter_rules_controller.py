from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_route_filter_rule import PatchRouteFilterRule
from openapi_server.models.route_filter_rule import RouteFilterRule
from openapi_server.models.route_filter_rule_list_result import RouteFilterRuleListResult
from openapi_server import util


async def route_filter_rules_create_or_update(request: web.Request, resource_group_name, route_filter_name, rule_name, api_version, subscription_id, route_filter_rule_parameters) -> web.Response:
    """route_filter_rules_create_or_update

    Creates or updates a route in the specified route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param rule_name: The name of the route filter rule.
    :type rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param route_filter_rule_parameters: Parameters supplied to the create or update route filter rule operation.
    :type route_filter_rule_parameters: dict | bytes

    """
    route_filter_rule_parameters = RouteFilterRule.from_dict(route_filter_rule_parameters)
    return web.Response(status=200)


async def route_filter_rules_delete(request: web.Request, resource_group_name, route_filter_name, rule_name, api_version, subscription_id) -> web.Response:
    """route_filter_rules_delete

    Deletes the specified rule from a route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_filter_rules_get(request: web.Request, resource_group_name, route_filter_name, rule_name, api_version, subscription_id) -> web.Response:
    """route_filter_rules_get

    Gets the specified rule from a route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_filter_rules_list_by_route_filter(request: web.Request, resource_group_name, route_filter_name, api_version, subscription_id) -> web.Response:
    """route_filter_rules_list_by_route_filter

    Gets all RouteFilterRules in a route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_filter_rules_update(request: web.Request, resource_group_name, route_filter_name, rule_name, api_version, subscription_id, route_filter_rule_parameters) -> web.Response:
    """route_filter_rules_update

    Updates a route in the specified route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param rule_name: The name of the route filter rule.
    :type rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param route_filter_rule_parameters: Parameters supplied to the update route filter rule operation.
    :type route_filter_rule_parameters: dict | bytes

    """
    route_filter_rule_parameters = PatchRouteFilterRule.from_dict(route_filter_rule_parameters)
    return web.Response(status=200)
