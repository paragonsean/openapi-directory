from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_wireless_failed_connections200_response_inner import GetNetworkWirelessFailedConnections200ResponseInner
from openapi_server import util


async def get_network_wireless_failed_connections_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, serial=None, client_id=None) -> web.Response:
    """List of all failed client connection events on this network in a given time range

    List of all failed client connection events on this network in a given time range

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param serial: Filter by AP
    :type serial: str
    :param client_id: Filter by client MAC
    :type client_id: str

    """
    return web.Response(status=200)
