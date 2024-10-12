from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_security_events(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the security events (intrusion detection only) for a network

    List the security events (intrusion detection only) for a network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_security_events(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the security events (intrusion detection only) for an organization

    List the security events (intrusion detection only) for an organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)
