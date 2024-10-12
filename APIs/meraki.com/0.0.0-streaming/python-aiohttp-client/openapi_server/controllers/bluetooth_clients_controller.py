from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_bluetooth_client(request: web.Request, network_id, bluetooth_client_id, include_connectivity_history=None, connectivity_history_timespan=None) -> web.Response:
    """Return a Bluetooth client

    Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.

    :param network_id: 
    :type network_id: str
    :param bluetooth_client_id: 
    :type bluetooth_client_id: str
    :param include_connectivity_history: Include the connectivity history for this client
    :type include_connectivity_history: bool
    :param connectivity_history_timespan: The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.
    :type connectivity_history_timespan: int

    """
    return web.Response(status=200)


async def get_network_bluetooth_clients(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None, include_connectivity_history=None) -> web.Response:
    """List the Bluetooth clients seen by APs in this network

    List the Bluetooth clients seen by APs in this network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param include_connectivity_history: Include the connectivity history for this client
    :type include_connectivity_history: bool

    """
    return web.Response(status=200)
