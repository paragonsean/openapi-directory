from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_loss_and_latency_history_2(request: web.Request, serial, ip, t0=None, t1=None, timespan=None, resolution=None, uplink=None) -> web.Response:
    """Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

    Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

    :param serial: 
    :type serial: str
    :param ip: The destination IP used to obtain the requested stats. This is required.
    :type ip: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    :type resolution: int
    :param uplink: The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    :type uplink: str

    """
    return web.Response(status=200)
