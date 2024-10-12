from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_wireless_client_connectivity_events_2(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None, types=None, included_severities=None, band=None, ssid_number=None, device_serial=None) -> web.Response:
    """List the wireless connectivity events for a client within a network in the timespan.

    List the wireless connectivity events for a client within a network in the timespan.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param types: A list of event types to include. If not specified, events of all types will be returned. Valid types are &#39;assoc&#39;, &#39;disassoc&#39;, &#39;auth&#39;, &#39;deauth&#39;, &#39;dns&#39;, &#39;dhcp&#39;, &#39;roam&#39;, &#39;connection&#39; and/or &#39;sticky&#39;.
    :type types: List[str]
    :param included_severities: A list of severities to include. If not specified, events of all severities will be returned. Valid severities are &#39;good&#39;, &#39;info&#39;, &#39;warn&#39; and/or &#39;bad&#39;.
    :type included_severities: List[str]
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39;, &#39;6&#39;).
    :type band: str
    :param ssid_number: An SSID number to include. If not specified, events for all SSIDs will be returned.
    :type ssid_number: int
    :param device_serial: Filter results by an AP&#39;s serial number.
    :type device_serial: str

    """
    return web.Response(status=200)
