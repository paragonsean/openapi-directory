from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_component_available_features import ApplicationInsightsComponentAvailableFeatures
from openapi_server.models.application_insights_component_billing_features import ApplicationInsightsComponentBillingFeatures
from openapi_server.models.application_insights_component_feature_capabilities import ApplicationInsightsComponentFeatureCapabilities
from openapi_server.models.application_insights_component_quota_status import ApplicationInsightsComponentQuotaStatus
from openapi_server import util


async def component_available_features_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """component_available_features_get

    Returns all available features of the application insights component.

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


async def component_current_billing_features_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """component_current_billing_features_get

    Returns current billing features for an Application Insights component.

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


async def component_current_billing_features_update(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, billing_features_properties) -> web.Response:
    """component_current_billing_features_update

    Update current billing features for an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param billing_features_properties: Properties that need to be specified to update billing features for an Application Insights component.
    :type billing_features_properties: dict | bytes

    """
    billing_features_properties = ApplicationInsightsComponentBillingFeatures.from_dict(billing_features_properties)
    return web.Response(status=200)


async def component_feature_capabilities_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """component_feature_capabilities_get

    Returns feature capabilities of the application insights component.

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


async def component_quota_status_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """component_quota_status_get

    Returns daily data volume cap (quota) status for an Application Insights component.

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
