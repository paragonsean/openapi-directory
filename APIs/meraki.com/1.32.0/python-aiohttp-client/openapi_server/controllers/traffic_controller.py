from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_traffic_1(request: web.Request, network_id, t0=None, timespan=None, device_type=None) -> web.Response:
    """Return the traffic analysis data for this network

    Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
    :type timespan: float
    :param device_type: Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage.
    :type device_type: str

    """
    return web.Response(status=200)
