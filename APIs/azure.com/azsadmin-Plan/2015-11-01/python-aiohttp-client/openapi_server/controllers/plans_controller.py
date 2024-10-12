from typing import List, Dict
from aiohttp import web

from openapi_server.models.plan import Plan
from openapi_server.models.plan_list import PlanList
from openapi_server.models.plans_list_metric_definitions200_response import PlansListMetricDefinitions200Response
from openapi_server.models.plans_list_metrics200_response import PlansListMetrics200Response
from openapi_server import util


async def plans_create_or_update(request: web.Request, subscription_id, resource_group_name, plan, api_version, new_plan) -> web.Response:
    """plans_create_or_update

    Create or update the plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param plan: Name of the plan.
    :type plan: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param new_plan: New plan.
    :type new_plan: dict | bytes

    """
    new_plan = Plan.from_dict(new_plan)
    return web.Response(status=200)


async def plans_delete(request: web.Request, subscription_id, resource_group_name, plan, api_version) -> web.Response:
    """plans_delete

    Delete the specified plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param plan: Name of the plan.
    :type plan: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def plans_get(request: web.Request, subscription_id, resource_group_name, plan, api_version) -> web.Response:
    """plans_get

    Get the specified plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param plan: Name of the plan.
    :type plan: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def plans_list(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """plans_list

    Get the list of plans under a resource group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def plans_list_all(request: web.Request, subscription_id, api_version) -> web.Response:
    """plans_list_all

    List all plans across all subscriptions.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def plans_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, plan, api_version) -> web.Response:
    """plans_list_metric_definitions

    Get the metric definitions of the specified plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param plan: Name of the plan.
    :type plan: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def plans_list_metrics(request: web.Request, subscription_id, resource_group_name, plan, api_version) -> web.Response:
    """plans_list_metrics

    Get the metrics of the specified plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param plan: Name of the plan.
    :type plan: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
