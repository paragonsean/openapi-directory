from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_rule_resource import AlertRuleResource
from openapi_server.models.alert_rule_resource_patch import AlertRuleResourcePatch
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def alert_rules_update(request: web.Request, subscription_id, resource_group_name, rule_name, api_version, alert_rules_resource) -> web.Response:
    """alert_rules_update

    Updates an existing AlertRuleResource. To update other fields use the CreateOrUpdate method.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param alert_rules_resource: Parameters supplied to the operation.
    :type alert_rules_resource: dict | bytes

    """
    alert_rules_resource = AlertRuleResourcePatch.from_dict(alert_rules_resource)
    return web.Response(status=200)
