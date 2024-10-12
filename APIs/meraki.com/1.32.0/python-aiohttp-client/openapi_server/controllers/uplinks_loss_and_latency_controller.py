from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server import util


async def get_organization_devices_uplinks_loss_and_latency_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None, uplink=None, ip=None) -> web.Response:
    """Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    :type timespan: float
    :param uplink: Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    :type uplink: str
    :param ip: Optional filter for a specific destination IP. Default will return all destination IPs.
    :type ip: str

    """
    return web.Response(status=200)
