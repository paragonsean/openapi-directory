from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_clients_bandwidth_usage_history200_response_inner import GetOrganizationClientsBandwidthUsageHistory200ResponseInner
from openapi_server import util


async def get_network_clients_bandwidth_usage_history_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

    Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_clients_bandwidth_usage_history_2(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

    Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)
