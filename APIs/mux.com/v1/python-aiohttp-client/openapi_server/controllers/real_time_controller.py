from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_real_time_breakdown_response import GetRealTimeBreakdownResponse
from openapi_server.models.get_real_time_histogram_timeseries_response import GetRealTimeHistogramTimeseriesResponse
from openapi_server.models.get_real_time_timeseries_response import GetRealTimeTimeseriesResponse
from openapi_server.models.list_real_time_dimensions_response import ListRealTimeDimensionsResponse
from openapi_server.models.list_real_time_metrics_response import ListRealTimeMetricsResponse
from openapi_server import util


async def get_realtime_breakdown(request: web.Request, realtime_metric_id, dimension=None, timestamp=None, filters=None, order_by=None, order_direction=None) -> web.Response:
    """Get Real-Time Breakdown

    Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score. This API is now deprecated, please use the &#x60;Get Monitoring Breakdown&#x60; API.

    :param realtime_metric_id: ID of the Realtime Metric
    :type realtime_metric_id: str
    :param dimension: Dimension the specified value belongs to
    :type dimension: str
    :param timestamp: Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
    :type timestamp: int
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param order_by: Value to order the results by
    :type order_by: str
    :param order_direction: Sort order.
    :type order_direction: str

    """
    return web.Response(status=200)


async def get_realtime_histogram_timeseries(request: web.Request, realtime_histogram_metric_id, filters=None) -> web.Response:
    """Get Real-Time Histogram Timeseries

    Gets histogram timeseries information for a specific metric. This API is now deprecated, please use the &#x60;Get Monitoring Histogram Timeseries&#x60; API.

    :param realtime_histogram_metric_id: ID of the Realtime Histogram Metric
    :type realtime_histogram_metric_id: str
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]

    """
    return web.Response(status=200)


async def get_realtime_timeseries(request: web.Request, realtime_metric_id, filters=None, timestamp=None) -> web.Response:
    """Get Real-Time Timeseries

    Gets Time series information for a specific metric along with the number of concurrent viewers. This API is now deprecated, please use the &#x60;Get Monitoring Timeseries&#x60; API.

    :param realtime_metric_id: ID of the Realtime Metric
    :type realtime_metric_id: str
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param timestamp: Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago.
    :type timestamp: int

    """
    return web.Response(status=200)


async def list_realtime_dimensions(request: web.Request, ) -> web.Response:
    """List Real-Time Dimensions

    Lists available real-time dimensions. This API is now deprecated, please use the &#x60;List Monitoring Dimensions&#x60; API.


    """
    return web.Response(status=200)


async def list_realtime_metrics(request: web.Request, ) -> web.Response:
    """List Real-Time Metrics

    Lists available real-time metrics. This API is now deprecated, please use the &#x60;List Monitoring Metrics&#x60; API.


    """
    return web.Response(status=200)
