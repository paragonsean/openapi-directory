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


async def alerts_change_state(request: web.Request, scope, alert_id, api_version, new_state) -> web.Response:
    """alerts_change_state

    Change the state of an alert.

    :param scope: scope here is resourceId for which alert is created.
    :type scope: str
    :param alert_id: Unique ID of an alert instance.
    :type alert_id: str
    :param api_version: API version.
    :type api_version: str
    :param new_state: New state of the alert.
    :type new_state: str

    """
    return web.Response(status=200)


async def alerts_get_all(request: web.Request, scope, api_version, target_resource=None, target_resource_type=None, target_resource_group=None, monitor_service=None, monitor_condition=None, severity=None, alert_state=None, alert_rule=None, smart_group_id=None, include_context=None, include_egress_config=None, page_count=None, sort_by=None, sort_order=None, select=None, time_range=None, custom_time_range=None) -> web.Response:
    """alerts_get_all

    List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime. 

    :param scope: scope here is resourceId for which alert is created.
    :type scope: str
    :param api_version: API version.
    :type api_version: str
    :param target_resource: Filter by target resource( which is full ARM ID) Default value is select all.
    :type target_resource: str
    :param target_resource_type: Filter by target resource type. Default value is select all.
    :type target_resource_type: str
    :param target_resource_group: Filter by target resource group name. Default value is select all.
    :type target_resource_group: str
    :param monitor_service: Filter by monitor service which generates the alert instance. Default value is select all.
    :type monitor_service: str
    :param monitor_condition: Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all.
    :type monitor_condition: str
    :param severity: Filter by severity.  Default value is select all.
    :type severity: str
    :param alert_state: Filter by state of the alert instance. Default value is to select all.
    :type alert_state: str
    :param alert_rule: Filter by specific alert rule.  Default value is to select all.
    :type alert_rule: str
    :param smart_group_id: Filter the alerts list by the Smart Group Id. Default value is none.
    :type smart_group_id: str
    :param include_context: Include context which has contextual data specific to the monitor service. Default value is false&#39;
    :type include_context: bool
    :param include_egress_config: Include egress config which would be used for displaying the content in portal.  Default value is &#39;false&#39;.
    :type include_egress_config: bool
    :param page_count: Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \&quot;includeContent\&quot;  filter is selected, maximum value allowed is 25. Default value is 25.
    :type page_count: int
    :param sort_by: Sort the query results by input field,  Default value is &#39;lastModifiedDateTime&#39;.
    :type sort_by: str
    :param sort_order: Sort the query results order in either ascending or descending.  Default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others.
    :type sort_order: str
    :param select: This filter allows to selection of the fields(comma separated) which would  be part of the essential section. This would allow to project only the  required fields rather than getting entire content.  Default is to fetch all the fields in the essentials section.
    :type select: str
    :param time_range: Filter by time range by below listed values. Default value is 1 day.
    :type time_range: str
    :param custom_time_range: Filter by custom time range in the format &lt;start-time&gt;/&lt;end-time&gt;  where time is in (ISO-8601 format)&#39;. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none.
    :type custom_time_range: str

    """
    return web.Response(status=200)


async def alerts_get_by_id(request: web.Request, scope, alert_id, api_version) -> web.Response:
    """Get a specific alert.

    Get information related to a specific alert

    :param scope: scope here is resourceId for which alert is created.
    :type scope: str
    :param alert_id: Unique ID of an alert instance.
    :type alert_id: str
    :param api_version: API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def alerts_get_history(request: web.Request, scope, alert_id, api_version) -> web.Response:
    """alerts_get_history

    Get the history of an alert, which captures any monitor condition changes (Fired/Resolved) and alert state changes (New/Acknowledged/Closed).

    :param scope: scope here is resourceId for which alert is created.
    :type scope: str
    :param alert_id: Unique ID of an alert instance.
    :type alert_id: str
    :param api_version: API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def alerts_get_summary(request: web.Request, scope, groupby, api_version, include_smart_groups_count=None, target_resource=None, target_resource_type=None, target_resource_group=None, monitor_service=None, monitor_condition=None, severity=None, alert_state=None, alert_rule=None, time_range=None, custom_time_range=None) -> web.Response:
    """alerts_get_summary

    Get a summarized count of your alerts grouped by various parameters (e.g. grouping by &#39;Severity&#39; returns the count of alerts for each severity).

    :param scope: scope here is resourceId for which alert is created.
    :type scope: str
    :param groupby: This parameter allows the result set to be grouped by input fields. For example, groupby&#x3D;severity,alertstate.
    :type groupby: str
    :param api_version: API version.
    :type api_version: str
    :param include_smart_groups_count: Include count of the SmartGroups as part of the summary. Default value is &#39;false&#39;.
    :type include_smart_groups_count: bool
    :param target_resource: Filter by target resource( which is full ARM ID) Default value is select all.
    :type target_resource: str
    :param target_resource_type: Filter by target resource type. Default value is select all.
    :type target_resource_type: str
    :param target_resource_group: Filter by target resource group name. Default value is select all.
    :type target_resource_group: str
    :param monitor_service: Filter by monitor service which generates the alert instance. Default value is select all.
    :type monitor_service: str
    :param monitor_condition: Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all.
    :type monitor_condition: str
    :param severity: Filter by severity.  Default value is select all.
    :type severity: str
    :param alert_state: Filter by state of the alert instance. Default value is to select all.
    :type alert_state: str
    :param alert_rule: Filter by specific alert rule.  Default value is to select all.
    :type alert_rule: str
    :param time_range: Filter by time range by below listed values. Default value is 1 day.
    :type time_range: str
    :param custom_time_range: Filter by custom time range in the format &lt;start-time&gt;/&lt;end-time&gt;  where time is in (ISO-8601 format)&#39;. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none.
    :type custom_time_range: str

    """
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    List all operations available through Azure Alerts Management Resource Provider.

    :param api_version: API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def smart_groups_change_state(request: web.Request, subscription_id, smart_group_id, api_version, new_state) -> web.Response:
    """smart_groups_change_state

    Change the state of a Smart Group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param smart_group_id: Smart group unique id. 
    :type smart_group_id: str
    :param api_version: API version.
    :type api_version: str
    :param new_state: New state of the alert.
    :type new_state: str

    """
    return web.Response(status=200)


async def smart_groups_get_all(request: web.Request, subscription_id, api_version, target_resource=None, target_resource_group=None, target_resource_type=None, monitor_service=None, monitor_condition=None, severity=None, smart_group_state=None, time_range=None, page_count=None, sort_by=None, sort_order=None) -> web.Response:
    """Get all Smart Groups within a specified subscription

    List all the Smart Groups within a specified subscription. 

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: API version.
    :type api_version: str
    :param target_resource: Filter by target resource( which is full ARM ID) Default value is select all.
    :type target_resource: str
    :param target_resource_group: Filter by target resource group name. Default value is select all.
    :type target_resource_group: str
    :param target_resource_type: Filter by target resource type. Default value is select all.
    :type target_resource_type: str
    :param monitor_service: Filter by monitor service which generates the alert instance. Default value is select all.
    :type monitor_service: str
    :param monitor_condition: Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all.
    :type monitor_condition: str
    :param severity: Filter by severity.  Default value is select all.
    :type severity: str
    :param smart_group_state: Filter by state of the smart group. Default value is to select all.
    :type smart_group_state: str
    :param time_range: Filter by time range by below listed values. Default value is 1 day.
    :type time_range: str
    :param page_count: Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \&quot;includeContent\&quot;  filter is selected, maximum value allowed is 25. Default value is 25.
    :type page_count: int
    :param sort_by: Sort the query results by input field. Default value is sort by &#39;lastModifiedDateTime&#39;.
    :type sort_by: str
    :param sort_order: Sort the query results order in either ascending or descending.  Default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others.
    :type sort_order: str

    """
    return web.Response(status=200)


async def smart_groups_get_by_id(request: web.Request, subscription_id, smart_group_id, api_version) -> web.Response:
    """Get information related to a specific Smart Group.

    Get information related to a specific Smart Group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param smart_group_id: Smart group unique id. 
    :type smart_group_id: str
    :param api_version: API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def smart_groups_get_history(request: web.Request, subscription_id, smart_group_id, api_version) -> web.Response:
    """smart_groups_get_history

    Get the history a smart group, which captures any Smart Group state changes (New/Acknowledged/Closed) .

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param smart_group_id: Smart group unique id. 
    :type smart_group_id: str
    :param api_version: API version.
    :type api_version: str

    """
    return web.Response(status=200)
