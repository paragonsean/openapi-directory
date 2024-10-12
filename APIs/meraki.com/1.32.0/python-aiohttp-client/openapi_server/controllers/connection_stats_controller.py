from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_device_wireless_connection_stats200_response import GetDeviceWirelessConnectionStats200Response
from openapi_server.models.get_network_wireless_connection_stats200_response import GetNetworkWirelessConnectionStats200Response
from openapi_server import util


async def get_device_wireless_connection_stats_1(request: web.Request, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for a given AP on this network

    Aggregated connectivity info for a given AP on this network

    :param serial: 
    :type serial: str
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

    """
    return web.Response(status=200)


async def get_network_wireless_client_connection_stats_2(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for a given client on this network

    Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
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

    """
    return web.Response(status=200)


async def get_network_wireless_clients_connection_stats_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network, grouped by clients

    Aggregated connectivity info for this network, grouped by clients

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

    """
    return web.Response(status=200)


async def get_network_wireless_connection_stats_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network

    Aggregated connectivity info for this network

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

    """
    return web.Response(status=200)


async def get_network_wireless_devices_connection_stats_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network, grouped by node

    Aggregated connectivity info for this network, grouped by node

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

    """
    return web.Response(status=200)
