from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events_results import EventsResults
from openapi_server.models.metrics_result import MetricsResult
from openapi_server.models.query_body import QueryBody
from openapi_server.models.query_results import QueryResults
from openapi_server import util


async def events_get(request: web.Request, subscription_id, resource_group_name, application_name, event_type, event_id, api_version, timespan=None) -> web.Response:
    """Get an event

    Gets the data for a single event

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param event_type: The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types.
    :type event_type: str
    :param event_id: ID of event.
    :type event_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param timespan: Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression.
    :type timespan: str

    """
    return web.Response(status=200)


async def events_get_by_type(request: web.Request, subscription_id, resource_group_name, application_name, event_type, api_version, timespan=None, filter=None, search=None, orderby=None, select=None, skip=None, top=None, format=None, count=None, apply=None) -> web.Response:
    """Execute OData query

    Executes an OData query for events

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param event_type: The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types.
    :type event_type: str
    :param api_version: Client API version.
    :type api_version: str
    :param timespan: Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression.
    :type timespan: str
    :param filter: An expression used to filter the returned events
    :type filter: str
    :param search: A free-text search expression to match for whether a particular event should be returned
    :type search: str
    :param orderby: A comma-separated list of properties with \\\&quot;asc\\\&quot; (the default) or \\\&quot;desc\\\&quot; to control the order of returned events
    :type orderby: str
    :param select: Limits the properties to just those requested on each returned event
    :type select: str
    :param skip: The number of items to skip over before returning events
    :type skip: int
    :param top: The number of events to return
    :type top: int
    :param format: Format for the returned events
    :type format: str
    :param count: Request a count of matching items included with the returned events
    :type count: bool
    :param apply: An expression used for aggregation over returned events
    :type apply: str

    """
    return web.Response(status=200)


async def events_get_odata_metadata(request: web.Request, subscription_id, resource_group_name, application_name, api_version) -> web.Response:
    """Get OData metadata

    Gets OData EDMX metadata describing the event data model

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def metrics_get(request: web.Request, subscription_id, resource_group_name, application_name, metric_id, api_version, timespan=None, interval=None, aggregation=None, segment=None, top=None, orderby=None, filter=None) -> web.Response:
    """Retrieve metric data

    Gets metric values for a single metric

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param metric_id: ID of the metric. This is either a standard AI metric, or an application-specific custom metric.
    :type metric_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param timespan: The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response.
    :type timespan: str
    :param interval: The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response.
    :type interval: str
    :param aggregation: The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used.
    :type aggregation: List[str]
    :param segment: The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter.
    :type segment: List[str]
    :param top: The number of segments to return.  This value is only valid when segment is specified.
    :type top: int
    :param orderby: The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified.
    :type orderby: str
    :param filter: An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving.
    :type filter: str

    """
    return web.Response(status=200)


async def metrics_get_metadata(request: web.Request, subscription_id, resource_group_name, application_name, api_version) -> web.Response:
    """Retrieve metric metadata

    Gets metadata describing the available metrics

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def query_execute(request: web.Request, subscription_id, resource_group_name, application_name, api_version, body) -> web.Response:
    """Execute an Analytics query

    Executes an Analytics query for data. [Here](https://dev.applicationinsights.io/documentation/Using-the-API/Query) is an example for using POST with an Analytics query.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param body: The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
    :type body: dict | bytes

    """
    body = QueryBody.from_dict(body)
    return web.Response(status=200)


async def query_get(request: web.Request, subscription_id, resource_group_name, application_name, query, api_version, timespan=None) -> web.Response:
    """Execute an Analytics query

    Executes an Analytics query for data

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: Name of the Application Insights application.
    :type application_name: str
    :param query: The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
    :type query: str
    :param api_version: Client API version.
    :type api_version: str
    :param timespan: Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression.
    :type timespan: str

    """
    return web.Response(status=200)
