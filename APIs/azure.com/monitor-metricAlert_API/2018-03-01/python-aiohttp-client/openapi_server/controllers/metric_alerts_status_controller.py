from typing import List, Dict
from aiohttp import web

from openapi_server.models.metric_alert_status_collection import MetricAlertStatusCollection
from openapi_server.models.metric_alerts_list_by_subscription_default_response import MetricAlertsListBySubscriptionDefaultResponse
from openapi_server import util


async def metric_alerts_status_list(request: web.Request, subscription_id, resource_group_name, rule_name, api_version) -> web.Response:
    """metric_alerts_status_list

    Retrieve an alert rule status.

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


async def metric_alerts_status_list_by_name(request: web.Request, subscription_id, resource_group_name, rule_name, status_name, api_version) -> web.Response:
    """metric_alerts_status_list_by_name

    Retrieve an alert rule status.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param status_name: The name of the status.
    :type status_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
