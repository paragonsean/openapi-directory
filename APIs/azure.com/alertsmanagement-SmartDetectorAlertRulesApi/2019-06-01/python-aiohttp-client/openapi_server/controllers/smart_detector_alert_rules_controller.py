from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_rule import AlertRule
from openapi_server.models.alert_rule_patch_object import AlertRulePatchObject
from openapi_server.models.alert_rules_list import AlertRulesList
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def smart_detector_alert_rules_create_or_update(request: web.Request, subscription_id, resource_group_name, alert_rule_name, api_version, parameters) -> web.Response:
    """smart_detector_alert_rules_create_or_update

    Create or update a Smart Detector alert rule.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param alert_rule_name: The name of the alert rule.
    :type alert_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = AlertRule.from_dict(parameters)
    return web.Response(status=200)


async def smart_detector_alert_rules_delete(request: web.Request, subscription_id, resource_group_name, alert_rule_name, api_version) -> web.Response:
    """smart_detector_alert_rules_delete

    Delete an existing Smart Detector alert rule.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param alert_rule_name: The name of the alert rule.
    :type alert_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def smart_detector_alert_rules_get(request: web.Request, subscription_id, resource_group_name, alert_rule_name, api_version, expand_detector=None) -> web.Response:
    """smart_detector_alert_rules_get

    Get a specific Smart Detector alert rule.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param alert_rule_name: The name of the alert rule.
    :type alert_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param expand_detector: Indicates if Smart Detector should be expanded.
    :type expand_detector: bool

    """
    return web.Response(status=200)


async def smart_detector_alert_rules_list(request: web.Request, subscription_id, api_version, expand_detector=None) -> web.Response:
    """smart_detector_alert_rules_list

    List all the existing Smart Detector alert rules within the subscription.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param expand_detector: Indicates if Smart Detector should be expanded.
    :type expand_detector: bool

    """
    return web.Response(status=200)


async def smart_detector_alert_rules_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, expand_detector=None) -> web.Response:
    """smart_detector_alert_rules_list_by_resource_group

    List all the existing Smart Detector alert rules within the subscription and resource group.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param expand_detector: Indicates if Smart Detector should be expanded.
    :type expand_detector: bool

    """
    return web.Response(status=200)


async def smart_detector_alert_rules_patch(request: web.Request, subscription_id, resource_group_name, alert_rule_name, api_version, parameters) -> web.Response:
    """smart_detector_alert_rules_patch

    Patch a specific Smart Detector alert rule.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param alert_rule_name: The name of the alert rule.
    :type alert_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = AlertRulePatchObject.from_dict(parameters)
    return web.Response(status=200)
