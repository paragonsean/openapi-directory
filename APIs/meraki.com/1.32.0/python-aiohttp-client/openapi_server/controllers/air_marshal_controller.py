from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_wireless_air_marshal_1(request: web.Request, network_id, t0=None, timespan=None) -> web.Response:
    """List Air Marshal scan results from a network

    List Air Marshal scan results from a network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float

    """
    return web.Response(status=200)
