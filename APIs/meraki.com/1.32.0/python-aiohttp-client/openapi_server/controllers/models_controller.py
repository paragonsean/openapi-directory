from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_summary_top_devices_models_by_usage200_response_inner import GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner
from openapi_server import util


async def get_organization_summary_top_devices_models_by_usage_4(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range. Default unit is megabytes.

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
