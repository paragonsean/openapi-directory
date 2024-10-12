from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_metric_response import ListMetricResponse
from openapi_server.models.metric_enum_stream_direction import MetricEnumStreamDirection
from openapi_server.models.metric_enum_twilio_edge import MetricEnumTwilioEdge
from openapi_server import util


async def list_metric(request: web.Request, call_sid, edge=None, direction=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_metric

    Get a list of Call Metrics for a Call.

    :param call_sid: The unique SID identifier of the Call.
    :type call_sid: str
    :param edge: The Edge of this Metric. One of &#x60;unknown_edge&#x60;, &#x60;carrier_edge&#x60;, &#x60;sip_edge&#x60;, &#x60;sdk_edge&#x60; or &#x60;client_edge&#x60;.
    :type edge: str
    :param direction: The Direction of this Metric. One of &#x60;unknown&#x60;, &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;.
    :type direction: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
