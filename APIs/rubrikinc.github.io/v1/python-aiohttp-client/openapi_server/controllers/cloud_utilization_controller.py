from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_out_forecast_request import CloudOutForecastRequest
from openapi_server.models.cloud_out_forecast_summary import CloudOutForecastSummary
from openapi_server import util


async def do_cloud_out_forecast(request: web.Request, body) -> web.Response:
    """Forecast of the cloud utilization for CloudOut

    Forecast of the cloud storage and compute utilization on cloud archival location according to the SLA Domain parameters.

    :param body: Object that contains the CloudOut forecast request.
    :type body: dict | bytes

    """
    body = CloudOutForecastRequest.from_dict(body)
    return web.Response(status=200)
