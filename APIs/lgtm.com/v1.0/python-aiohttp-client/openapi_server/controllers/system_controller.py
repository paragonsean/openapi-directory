from typing import List, Dict
from aiohttp import web

from openapi_server.models.health import Health
from openapi_server.models.metric import Metric
from openapi_server.models.metrics_list import MetricsList
from openapi_server import util


async def get_health(request: web.Request, ) -> web.Response:
    """Get a summary of the application&#39;s health

    Return an indication of whether the application is working as expected (up) or needs  attention (down).  \\&gt; The &#x60;description&#x60; and &#x60;details&#x60; fields are reported only if the request includes an access token for a user account that has administration rights for this LGTM server. 


    """
    return web.Response(status=200)


async def get_metric(request: web.Request, metric_id) -> web.Response:
    """Get the computed values of the specified metric

    LGTM administrators can download usage data using this endpoint. The response includes up to 1000 values for the specified metric and reports the date-time that each value was calculated. There is normally one value per day. 

    :param metric_id: The identifier of the metric.
    :type metric_id: str

    """
    return web.Response(status=200)


async def get_metrics(request: web.Request, ) -> web.Response:
    """Get the identifiers and descriptions of the usage metrics

    LGTM administrators can use this endpoint to list the usage metrics that are available to download. 


    """
    return web.Response(status=200)
