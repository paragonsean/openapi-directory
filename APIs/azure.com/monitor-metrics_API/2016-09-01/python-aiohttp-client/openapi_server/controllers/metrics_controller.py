from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.metric_collection import MetricCollection
from openapi_server import util


async def metrics_list(request: web.Request, resource_uri, api_version, filter=None) -> web.Response:
    """metrics_list

    Lists the metric values for a resource.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: Reduces the set of data collected.&lt;br&gt;The filter is optional. If present it must contain a list of metric names to retrieve of the form: *(name.value eq &#39;metricName&#39; [or name.value eq &#39;metricName&#39; or ...])*. Optionally, the filter can contain conditions for the following attributes *aggregationType*, *startTime*, *endTime*, and *timeGrain* of the form *attributeName operator value*. Where operator is one of *ne*, *eq*, *gt*, *lt*.&lt;br&gt;Several conditions can be combined with parentheses and logical operators, e.g: *and*, *or*.&lt;br&gt;Some example filter expressions are:&lt;br&gt;- $filter&#x3D;(name.value eq &#39;RunsSucceeded&#39;) and aggregationType eq &#39;Total&#39; and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1M&#39;,&lt;br&gt;- $filter&#x3D;(name.value eq &#39;RunsSucceeded&#39;) and (aggregationType eq &#39;Total&#39; or aggregationType eq &#39;Average&#39;) and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1H&#39;,&lt;br&gt;- $filter&#x3D;(name.value eq &#39;ActionsCompleted&#39; or name.value eq &#39;RunsSucceeded&#39;) and (aggregationType eq &#39;Total&#39; or aggregationType eq &#39;Average&#39;) and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1M&#39;.&lt;br&gt;&lt;br&gt;**NOTE**: When a metrics query comes in with multiple metrics, but with no aggregation types defined, the service will pick the Primary aggregation type of the first metrics to be used as the default aggregation type for all the metrics.
    :type filter: str

    """
    return web.Response(status=200)
