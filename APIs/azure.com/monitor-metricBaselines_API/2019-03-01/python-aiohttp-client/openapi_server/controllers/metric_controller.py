from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.metric_baselines_response import MetricBaselinesResponse
from openapi_server import util


async def baselines_list_0(request: web.Request, resource_uri, api_version, metricnames=None, metricnamespace=None, timespan=None, interval=None, aggregation=None, sensitivities=None, filter=None, result_type=None) -> web.Response:
    """baselines_list_0

    **Lists the metric baseline values for a resource**.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param metricnames: The names of the metrics (comma separated) to retrieve.
    :type metricnames: str
    :param metricnamespace: Metric namespace to query metric definitions for.
    :type metricnamespace: str
    :param timespan: The timespan of the query. It is a string with the following format &#39;startDateTime_ISO/endDateTime_ISO&#39;.
    :type timespan: str
    :param interval: The interval (i.e. timegrain) of the query.
    :type interval: str
    :param aggregation: The list of aggregation types (comma separated) to retrieve.
    :type aggregation: str
    :param sensitivities: The list of sensitivities (comma separated) to retrieve.
    :type sensitivities: str
    :param filter: The **$filter** is used to reduce the set of metric data returned.&lt;br&gt;Example:&lt;br&gt;Metric contains metadata A, B and C.&lt;br&gt;- Return all time series of C where A &#x3D; a1 and B &#x3D; b1 or b2&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**&lt;br&gt;- Invalid variant:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B &#x3D; ‘b2’**&lt;br&gt;This is invalid because the logical or operator cannot separate two different metadata names.&lt;br&gt;- Return all time series where A &#x3D; a1, B &#x3D; b1 and C &#x3D; c1:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**&lt;br&gt;- Return all time series where A &#x3D; a1&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**.
    :type filter: str
    :param result_type: Allows retrieving only metadata of the baseline. On data request all information is retrieved.
    :type result_type: str

    """
    return web.Response(status=200)
