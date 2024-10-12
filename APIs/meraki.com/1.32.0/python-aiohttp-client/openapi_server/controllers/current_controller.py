from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server import util


async def get_network_sensor_alerts_current_overview_by_metric_2(request: web.Request, network_id) -> web.Response:
    """Return an overview of currently alerting sensors by metric

    Return an overview of currently alerting sensors by metric

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
