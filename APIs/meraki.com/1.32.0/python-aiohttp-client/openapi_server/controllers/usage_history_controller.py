from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_wireless_usage_history200_response_inner import GetNetworkWirelessUsageHistory200ResponseInner
from openapi_server import util


async def get_network_appliance_uplinks_usage_history_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get the sent and received bytes for each uplink of a network.

    Get the sent and received bytes for each uplink of a network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_client_usage_history_2(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client&#39;s daily usage history

    Return the client&#39;s daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_usage_history_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
    """Return AP usage over time for a device or network client

    Return AP usage over time for a device or network client

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
    :param client_id: Filter results by network client to return per-device AP usage over time inner joined by the queried client&#39;s connection history.
    :type client_id: str
    :param device_serial: Filter results by device. Requires :band.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int

    """
    return web.Response(status=200)
