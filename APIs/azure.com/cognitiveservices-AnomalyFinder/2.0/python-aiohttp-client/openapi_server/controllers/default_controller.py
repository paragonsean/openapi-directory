from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.entire_detect_response import EntireDetectResponse
from openapi_server.models.last_detect_response import LastDetectResponse
from openapi_server.models.request import Request
from openapi_server import util


async def entire_detect(request: web.Request, body) -> web.Response:
    """Find anomalies for the entire series in batch.

    The operation will generate a model using the entire series, each point will be detected with the same model. In this method, points before and after a certain point will be used to determine whether it&#39;s an anomaly. The entire detection can give user an overall status of the time series.

    :param body: Time series points and period if needed. Advanced model parameters can also be set in the request.
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)


async def last_detect(request: web.Request, body) -> web.Response:
    """Detect anomaly status of the latest point in time series.

    The operation will generate a model using points before the latest one, In this method, only history points are used for determine whether the target point is an anomaly. Latest point detecting matches the scenario of real-time monitoring of business metrics.

    :param body: Time series points and period if needed. Advanced model parameters can also be set in the request.
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)
