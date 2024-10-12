from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.incident import Incident
from openapi_server.models.incident_list_result import IncidentListResult
from openapi_server import util


async def alert_rule_incidents_get(request: web.Request, resource_group_name, rule_name, incident_name, api_version, subscription_id) -> web.Response:
    """alert_rule_incidents_get

    Gets an incident associated to an alert rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param rule_name: The name of the rule.
    :type rule_name: str
    :param incident_name: The name of the incident to retrieve.
    :type incident_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def alert_rule_incidents_list_by_alert_rule(request: web.Request, resource_group_name, rule_name, api_version, subscription_id) -> web.Response:
    """alert_rule_incidents_list_by_alert_rule

    Gets a list of incidents associated to an alert rule

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
