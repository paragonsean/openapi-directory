from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.response import Response
from openapi_server import util


async def metrics_list(request: web.Request, resource_uri, api_version, timespan=None, interval=None, metricnames=None, aggregation=None, top=None, orderby=None, filter=None, result_type=None, metricnamespace=None) -> web.Response:
    """metrics_list

    **Lists the metric values for a resource**.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param timespan: The timespan of the query. It is a string with the following format &#39;startDateTime_ISO/endDateTime_ISO&#39;.
    :type timespan: str
    :param interval: The interval (i.e. timegrain) of the query.
    :type interval: str
    :param metricnames: The names of the metrics (comma separated) to retrieve.
    :type metricnames: str
    :param aggregation: The list of aggregation types (comma separated) to retrieve.
    :type aggregation: str
    :param top: The maximum number of records to retrieve. Valid only if $filter is specified. Defaults to 10.
    :type top: int
    :param orderby: The aggregation to use for sorting results and the direction of the sort. Only one order can be specified. Examples: sum asc.
    :type orderby: str
    :param filter: The **$filter** is used to reduce the set of metric data returned.&lt;br&gt;Example:&lt;br&gt;Metric contains metadata A, B and C.&lt;br&gt;- Return all time series of C where A &#x3D; a1 and B &#x3D; b1 or b2&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**&lt;br&gt;- Invalid variant:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B &#x3D; ‘b2’**&lt;br&gt;This is invalid because the logical or operator cannot separate two different metadata names.&lt;br&gt;- Return all time series where A &#x3D; a1, B &#x3D; b1 and C &#x3D; c1:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**&lt;br&gt;- Return all time series where A &#x3D; a1&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**.
    :type filter: str
    :param result_type: Reduces the set of data collected. The syntax allowed depends on the operation. See the operation&#39;s description for details.
    :type result_type: str
    :param metricnamespace: Metric namespace to query metric definitions for.
    :type metricnamespace: str

    """
    return web.Response(status=200)
