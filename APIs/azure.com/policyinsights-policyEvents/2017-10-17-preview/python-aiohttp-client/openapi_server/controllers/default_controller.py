from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_events_query_results import PolicyEventsQueryResults
from openapi_server.models.query_failure import QueryFailure
from openapi_server import util


async def policy_events_get_metadata(request: web.Request, scope, api_version) -> web.Response:
    """policy_events_get_metadata

    Gets OData metadata XML document.

    :param scope: A valid scope, i.e. management group, subscription, resource group, or resource ID. Scope used has no effect on metadata returned.
    :type scope: str
    :param api_version: API version to use with the client requests.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_events_list_query_results_for_management_group(request: web.Request, policy_events_resource, management_groups_namespace, management_group_name, api_version, top=None, orderby=None, select=None, _from=None, to=None, filter=None, apply=None) -> web.Response:
    """policy_events_list_query_results_for_management_group

    Queries policy events for the resources under the management group.

    :param policy_events_resource: The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed.
    :type policy_events_resource: str
    :param management_groups_namespace: The namespace for Microsoft Management resource provider; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_name: Management group name.
    :type management_group_name: str
    :param api_version: API version to use with the client requests.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param orderby: Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;.
    :type orderby: str
    :param select: Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;.
    :type select: str
    :param _from: ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    :type _from: str
    :param to: ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    :type to: str
    :param filter: OData filter expression.
    :type filter: str
    :param apply: OData apply expression for aggregations.
    :type apply: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def policy_events_list_query_results_for_resource(request: web.Request, policy_events_resource, resource_id, api_version, top=None, orderby=None, select=None, _from=None, to=None, filter=None, apply=None) -> web.Response:
    """policy_events_list_query_results_for_resource

    Queries policy events for the resource.

    :param policy_events_resource: The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed.
    :type policy_events_resource: str
    :param resource_id: Resource ID.
    :type resource_id: str
    :param api_version: API version to use with the client requests.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param orderby: Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;.
    :type orderby: str
    :param select: Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;.
    :type select: str
    :param _from: ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    :type _from: str
    :param to: ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    :type to: str
    :param filter: OData filter expression.
    :type filter: str
    :param apply: OData apply expression for aggregations.
    :type apply: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def policy_events_list_query_results_for_resource_group(request: web.Request, policy_events_resource, subscription_id, resource_group_name, api_version, top=None, orderby=None, select=None, _from=None, to=None, filter=None, apply=None) -> web.Response:
    """policy_events_list_query_results_for_resource_group

    Queries policy events for the resources under the resource group.

    :param policy_events_resource: The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed.
    :type policy_events_resource: str
    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: API version to use with the client requests.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param orderby: Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;.
    :type orderby: str
    :param select: Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;.
    :type select: str
    :param _from: ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    :type _from: str
    :param to: ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    :type to: str
    :param filter: OData filter expression.
    :type filter: str
    :param apply: OData apply expression for aggregations.
    :type apply: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def policy_events_list_query_results_for_subscription(request: web.Request, policy_events_resource, subscription_id, api_version, top=None, orderby=None, select=None, _from=None, to=None, filter=None, apply=None) -> web.Response:
    """policy_events_list_query_results_for_subscription

    Queries policy events for the resources under the subscription.

    :param policy_events_resource: The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed.
    :type policy_events_resource: str
    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param api_version: API version to use with the client requests.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param orderby: Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;.
    :type orderby: str
    :param select: Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;.
    :type select: str
    :param _from: ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    :type _from: str
    :param to: ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    :type to: str
    :param filter: OData filter expression.
    :type filter: str
    :param apply: OData apply expression for aggregations.
    :type apply: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
