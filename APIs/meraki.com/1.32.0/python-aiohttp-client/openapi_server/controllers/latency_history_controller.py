from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_wireless_latency_history200_response_inner import GetNetworkWirelessLatencyHistory200ResponseInner
from openapi_server import util


async def get_network_wireless_client_latency_history_2(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Return the latency history for a client

    Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_wireless_latency_history_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None, access_category=None) -> web.Response:
    """Return average wireless latency over time for a network, device, or network client

    Return average wireless latency over time for a network, device, or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client.
    :type client_id: str
    :param device_serial: Filter results by device.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int
    :param access_category: Filter by access category.
    :type access_category: str

    """
    return web.Response(status=200)
