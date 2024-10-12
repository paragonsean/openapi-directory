from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_metric_timeseries_data_response import GetMetricTimeseriesDataResponse
from openapi_server.models.get_overall_values_response import GetOverallValuesResponse
from openapi_server.models.list_all_metric_values_response import ListAllMetricValuesResponse
from openapi_server.models.list_breakdown_values_response import ListBreakdownValuesResponse
from openapi_server.models.list_insights_response import ListInsightsResponse
from openapi_server import util


async def get_metric_timeseries_data(request: web.Request, metric_id, timeframe=None, filters=None, measurement=None, order_direction=None, group_by=None) -> web.Response:
    """Get metric timeseries data

    Returns timeseries data for a specific metric.  Each interval represented in the data array contains an array with the following values:   * the first element is the interval time   * the second element is the calculated metric value   * the third element is the number of views in the interval that have a valid metric value 

    :param metric_id: ID of the Metric
    :type metric_id: str
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param measurement: Measurement for the provided metric. If omitted, the default for the metric will be used.
    :type measurement: str
    :param order_direction: Sort order.
    :type order_direction: str
    :param group_by: Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the timeframe.  For timeframes of less than 90 minutes, the default granularity is &#x60;minute&#x60;. Between 90 minutes and 6 hours, the default granularity is &#x60;ten_minutes&#x60;. Between 6 hours and 15 days inclusive, the default granularity is &#x60;hour&#x60;. The granularity of timeframes that exceed 15 days is &#x60;day&#x60;. This default behavior is subject to change; it is strongly suggested that you explicitly specify the granularity. 
    :type group_by: str

    """
    return web.Response(status=200)


async def get_overall_values(request: web.Request, metric_id, timeframe=None, filters=None, measurement=None) -> web.Response:
    """Get Overall values

    Returns the overall value for a specific metric, as well as the total view count, watch time, and the Mux Global metric value for the metric.

    :param metric_id: ID of the Metric
    :type metric_id: str
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param measurement: Measurement for the provided metric. If omitted, the default for the metric will be used.
    :type measurement: str

    """
    return web.Response(status=200)


async def list_all_metric_values(request: web.Request, timeframe=None, filters=None, dimension=None, value=None) -> web.Response:
    """List all metric values

    List all of the values across every breakdown for a specific metric.

    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param dimension: Dimension the specified value belongs to
    :type dimension: str
    :param value: Value to show all available metrics for
    :type value: str

    """
    return web.Response(status=200)


async def list_breakdown_values(request: web.Request, metric_id, group_by=None, measurement=None, filters=None, limit=None, page=None, order_by=None, order_direction=None, timeframe=None) -> web.Response:
    """List breakdown values

    List the breakdown values for a specific metric.

    :param metric_id: ID of the Metric
    :type metric_id: str
    :param group_by: Breakdown value to group the results by
    :type group_by: str
    :param measurement: Measurement for the provided metric. If omitted, the default for the metric will be used.
    :type measurement: str
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param order_by: Value to order the results by
    :type order_by: str
    :param order_direction: Sort order.
    :type order_direction: str
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]

    """
    return web.Response(status=200)


async def list_insights(request: web.Request, metric_id, measurement=None, order_direction=None, timeframe=None) -> web.Response:
    """List Insights

    Returns a list of insights for a metric. These are the worst performing values across all breakdowns sorted by how much they negatively impact a specific metric.

    :param metric_id: ID of the Metric
    :type metric_id: str
    :param measurement: Measurement for the provided metric. If omitted, the default for the metric will be used.
    :type measurement: str
    :param order_direction: Sort order.
    :type order_direction: str
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]

    """
    return web.Response(status=200)
