from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_switch_ports_statuses_packets_3(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the packet counters for all the ports of a switch

    Return the packet counters for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)
