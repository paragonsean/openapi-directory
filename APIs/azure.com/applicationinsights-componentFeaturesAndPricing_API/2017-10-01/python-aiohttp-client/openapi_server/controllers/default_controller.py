from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_component_pricing_plan import ApplicationInsightsComponentPricingPlan
from openapi_server import util


async def component_current_pricing_plan_create_and_update(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, pricing_plan_properties) -> web.Response:
    """component_current_pricing_plan_create_and_update

    Replace current pricing plan for an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param pricing_plan_properties: Properties that need to be specified to update current pricing plan for an Application Insights component.
    :type pricing_plan_properties: dict | bytes

    """
    pricing_plan_properties = ApplicationInsightsComponentPricingPlan.from_dict(pricing_plan_properties)
    return web.Response(status=200)


async def component_current_pricing_plan_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """component_current_pricing_plan_get

    Returns the current pricing plan setting for an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def component_current_pricing_plan_update(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, pricing_plan_properties) -> web.Response:
    """component_current_pricing_plan_update

    Update current pricing plan for an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param pricing_plan_properties: Properties that need to be specified to update current pricing plan for an Application Insights component.
    :type pricing_plan_properties: dict | bytes

    """
    pricing_plan_properties = ApplicationInsightsComponentPricingPlan.from_dict(pricing_plan_properties)
    return web.Response(status=200)
