from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner
from openapi_server import util


async def get_network_sensor_alerts_current_overview_by_metric_4(request: web.Request, network_id) -> web.Response:
    """Return an overview of currently alerting sensors by metric

    Return an overview of currently alerting sensors by metric

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_overview_by_metric_3(request: web.Request, network_id, t0=None, t1=None, timespan=None, interval=None) -> web.Response:
    """Return an overview of alert occurrences over a timespan, by metric

    Return an overview of alert occurrences over a timespan, by metric

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
    :type interval: int

    """
    return web.Response(status=200)
