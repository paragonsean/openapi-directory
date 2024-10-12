from typing import List, Dict
from aiohttp import web

from openapi_server.models.metric_alert_resource import MetricAlertResource
from openapi_server.models.metric_alert_resource_collection import MetricAlertResourceCollection
from openapi_server.models.metric_alert_resource_patch import MetricAlertResourcePatch
from openapi_server.models.metric_alerts_list_by_subscription_default_response import MetricAlertsListBySubscriptionDefaultResponse
from openapi_server import util


async def metric_alerts_create_or_update(request: web.Request, subscription_id, resource_group_name, rule_name, api_version, parameters) -> web.Response:
    """metric_alerts_create_or_update

    Create or update an metric alert definition.

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
    parameters = MetricAlertResource.from_dict(parameters)
    return web.Response(status=200)


async def metric_alerts_delete(request: web.Request, subscription_id, resource_group_name, rule_name, api_version) -> web.Response:
    """metric_alerts_delete

    Delete an alert rule definition.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def metric_alerts_get(request: web.Request, subscription_id, resource_group_name, rule_name, api_version) -> web.Response:
    """metric_alerts_get

    Retrieve an alert rule definition.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def metric_alerts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """metric_alerts_list_by_resource_group

    Retrieve alert rule definitions in a resource group.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def metric_alerts_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """metric_alerts_list_by_subscription

    Retrieve alert rule definitions in a subscription.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def metric_alerts_update(request: web.Request, subscription_id, resource_group_name, rule_name, api_version, parameters) -> web.Response:
    """metric_alerts_update

    Update an metric alert definition.

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
    parameters = MetricAlertResourcePatch.from_dict(parameters)
    return web.Response(status=200)
