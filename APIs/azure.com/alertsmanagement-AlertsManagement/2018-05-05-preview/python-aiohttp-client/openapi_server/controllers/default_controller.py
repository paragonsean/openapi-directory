from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_modification import AlertModification
from openapi_server.models.alerts_list import AlertsList
from openapi_server.models.alerts_summary import AlertsSummary
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operations_list import OperationsList
from openapi_server.models.smart_group import SmartGroup
from openapi_server.models.smart_group_modification import SmartGroupModification
from openapi_server.models.smart_groups_list import SmartGroupsList
from openapi_server import util


async def alerts_change_state(request: web.Request, subscription_id, alert_id, api_version, new_state) -> web.Response:
    """alerts_change_state

    Change the state of the alert.

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param alert_id: Unique ID of an alert object.
    :type alert_id: str
    :param api_version: client API version
    :type api_version: str
    :param new_state: filter by state
    :type new_state: str

    """
    return web.Response(status=200)


async def alerts_get_all(request: web.Request, subscription_id, api_version, target_resource=None, target_resource_group=None, target_resource_type=None, monitor_service=None, monitor_condition=None, severity=None, alert_state=None, smart_group_id=None, include_payload=None, page_count=None, sort_by=None, sort_order=None, time_range=None) -> web.Response:
    """alerts_get_all

    List all the existing alerts, where the results can be selective by passing multiple filter parameters including time range and sorted on specific fields. 

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: client API version
    :type api_version: str
    :param target_resource: filter by target resource
    :type target_resource: str
    :param target_resource_group: filter by target resource group name
    :type target_resource_group: str
    :param target_resource_type: filter by target resource type
    :type target_resource_type: str
    :param monitor_service: filter by monitor service which is the source of the alert object.
    :type monitor_service: str
    :param monitor_condition: filter by monitor condition which is the state of the alert at monitor service
    :type monitor_condition: str
    :param severity: filter by severity
    :type severity: str
    :param alert_state: filter by state
    :type alert_state: str
    :param smart_group_id: filter by smart Group Id
    :type smart_group_id: str
    :param include_payload: include payload field content, default value is &#39;false&#39;.
    :type include_payload: bool
    :param page_count: number of items per page, default value is &#39;25&#39;.
    :type page_count: int
    :param sort_by: sort the query results by input field, default value is &#39;lastModifiedDateTime&#39;.
    :type sort_by: str
    :param sort_order: sort the query results order in either ascending or descending, default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others.
    :type sort_order: str
    :param time_range: filter by time range, default value is 1 day
    :type time_range: str

    """
    return web.Response(status=200)


async def alerts_get_by_id(request: web.Request, subscription_id, alert_id, api_version) -> web.Response:
    """Get a specific alert.

    Get information related to a specific alert

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param alert_id: Unique ID of an alert object.
    :type alert_id: str
    :param api_version: client API version
    :type api_version: str

    """
    return web.Response(status=200)


async def alerts_get_history(request: web.Request, subscription_id, alert_id, api_version) -> web.Response:
    """alerts_get_history

    Get the history of the changes of an alert.

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param alert_id: Unique ID of an alert object.
    :type alert_id: str
    :param api_version: client API version
    :type api_version: str

    """
    return web.Response(status=200)


async def alerts_get_summary(request: web.Request, subscription_id, api_version, target_resource_group=None, time_range=None) -> web.Response:
    """alerts_get_summary

    Summary of alerts with the count each severity.

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: client API version
    :type api_version: str
    :param target_resource_group: filter by target resource group name
    :type target_resource_group: str
    :param time_range: filter by time range, default value is 1 day
    :type time_range: str

    """
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    List all operations available through Azure Alerts Management Resource Provider.

    :param api_version: client API version
    :type api_version: str

    """
    return web.Response(status=200)


async def smart_groups_change_state(request: web.Request, subscription_id, smart_group_id, api_version, new_state) -> web.Response:
    """smart_groups_change_state

    Change the state from unresolved to resolved and all the alerts within the smart group will also be resolved.

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param smart_group_id: Smart Group Id
    :type smart_group_id: str
    :param api_version: client API version
    :type api_version: str
    :param new_state: filter by state
    :type new_state: str

    """
    return web.Response(status=200)


async def smart_groups_get_all(request: web.Request, subscription_id, api_version, target_resource=None, target_resource_group=None, target_resource_type=None, monitor_service=None, monitor_condition=None, severity=None, smart_group_state=None, time_range=None, page_count=None, sort_by=None, sort_order=None) -> web.Response:
    """Get all smartGroups within the subscription

    List all the smartGroups within the specified subscription. 

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: client API version
    :type api_version: str
    :param target_resource: filter by target resource
    :type target_resource: str
    :param target_resource_group: filter by target resource group name
    :type target_resource_group: str
    :param target_resource_type: filter by target resource type
    :type target_resource_type: str
    :param monitor_service: filter by monitor service which is the source of the alert object.
    :type monitor_service: str
    :param monitor_condition: filter by monitor condition which is the state of the alert at monitor service
    :type monitor_condition: str
    :param severity: filter by severity
    :type severity: str
    :param smart_group_state: filter by state
    :type smart_group_state: str
    :param time_range: filter by time range, default value is 1 day
    :type time_range: str
    :param page_count: number of items per page, default value is &#39;25&#39;.
    :type page_count: int
    :param sort_by: sort the query results by input field, default value is &#39;lastModifiedDateTime&#39;.
    :type sort_by: str
    :param sort_order: sort the query results order in either ascending or descending, default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others.
    :type sort_order: str

    """
    return web.Response(status=200)


async def smart_groups_get_by_id(request: web.Request, subscription_id, smart_group_id, api_version) -> web.Response:
    """Get information of smart alerts group.

    Get details of smart group.

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param smart_group_id: Smart Group Id
    :type smart_group_id: str
    :param api_version: client API version
    :type api_version: str

    """
    return web.Response(status=200)


async def smart_groups_get_history(request: web.Request, subscription_id, smart_group_id, api_version) -> web.Response:
    """smart_groups_get_history

    Get the history of the changes of smart group.

    :param subscription_id: subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param smart_group_id: Smart Group Id
    :type smart_group_id: str
    :param api_version: client API version
    :type api_version: str

    """
    return web.Response(status=200)
