from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_insight_application_health_by_time200_response_inner import GetNetworkInsightApplicationHealthByTime200ResponseInner
from openapi_server.models.get_organization_insight_applications200_response_inner import GetOrganizationInsightApplications200ResponseInner
from openapi_server import util


async def get_network_insight_application_health_by_time_1(request: web.Request, network_id, application_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get application health by time

    Get application health by time

    :param network_id: 
    :type network_id: str
    :param application_id: 
    :type application_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_organization_insight_applications_1(request: web.Request, organization_id) -> web.Response:
    """List all Insight tracked applications

    List all Insight tracked applications

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
