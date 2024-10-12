from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_monitoring_breakdown_response import GetMonitoringBreakdownResponse
from openapi_server.models.get_monitoring_breakdown_timeseries_response import GetMonitoringBreakdownTimeseriesResponse
from openapi_server.models.get_monitoring_histogram_timeseries_response import GetMonitoringHistogramTimeseriesResponse
from openapi_server.models.get_monitoring_timeseries_response import GetMonitoringTimeseriesResponse
from openapi_server.models.list_monitoring_dimensions_response import ListMonitoringDimensionsResponse
from openapi_server.models.list_monitoring_metrics_response import ListMonitoringMetricsResponse
from openapi_server import util


async def get_monitoring_breakdown(request: web.Request, monitoring_metric_id, dimension=None, timestamp=None, filters=None, order_by=None, order_direction=None) -> web.Response:
    """Get Monitoring Breakdown

    Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.

    :param monitoring_metric_id: ID of the Monitoring Metric
    :type monitoring_metric_id: str
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


async def get_monitoring_breakdown_timeseries(request: web.Request, monitoring_metric_id, dimension=None, timeframe=None, filters=None, limit=None, order_by=None, order_direction=None) -> web.Response:
    """Get Monitoring Breakdown Timeseries

    Gets timeseries of breakdown information for a specific dimension and metric. Each datapoint in the response represents 5 seconds worth of data.

    :param monitoring_metric_id: ID of the Monitoring Metric
    :type monitoring_metric_id: str
    :param dimension: Dimension the specified value belongs to
    :type dimension: str
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  The default for this is the last 60 seconds of available data. Timeframes larger than 10 minutes are not allowed, and must be within the last 24 hours. 
    :type timeframe: List[str]
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param limit: Number of items to include in each timestamp&#39;s &#x60;value&#x60; list.  The default is 10, and the maximum is 100. 
    :type limit: int
    :param order_by: Value to order the results by
    :type order_by: str
    :param order_direction: Sort order.
    :type order_direction: str

    """
    return web.Response(status=200)


async def get_monitoring_histogram_timeseries(request: web.Request, monitoring_histogram_metric_id, filters=None) -> web.Response:
    """Get Monitoring Histogram Timeseries

    Gets histogram timeseries information for a specific metric.

    :param monitoring_histogram_metric_id: ID of the Monitoring Histogram Metric
    :type monitoring_histogram_metric_id: str
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]

    """
    return web.Response(status=200)


async def get_monitoring_timeseries(request: web.Request, monitoring_metric_id, filters=None, timestamp=None) -> web.Response:
    """Get Monitoring Timeseries

    Gets Time series information for a specific metric along with the number of concurrent viewers.

    :param monitoring_metric_id: ID of the Monitoring Metric
    :type monitoring_metric_id: str
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param timestamp: Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago.
    :type timestamp: int

    """
    return web.Response(status=200)


async def list_monitoring_dimensions(request: web.Request, ) -> web.Response:
    """List Monitoring Dimensions

    Lists available monitoring dimensions.


    """
    return web.Response(status=200)


async def list_monitoring_metrics(request: web.Request, ) -> web.Response:
    """List Monitoring Metrics

    Lists available monitoring metrics.


    """
    return web.Response(status=200)
