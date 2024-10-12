from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_api_requests_overview_response_codes_by_interval200_response_inner import GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner
from openapi_server import util


async def get_organization_api_requests_overview_response_codes_by_interval_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None, interval=None, version=None, operation_ids=None, source_ips=None, admin_ids=None, user_agent=None) -> web.Response:
    """Tracks organizations&#39; API requests by response code across a given time period

    Tracks organizations&#39; API requests by response code across a given time period

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
    :type interval: int
    :param version: Filter by API version of the endpoint. Allowable values are: [0, 1]
    :type version: int
    :param operation_ids: Filter by operation ID of the endpoint
    :type operation_ids: List[str]
    :param source_ips: Filter by source IP that made the API request
    :type source_ips: List[str]
    :param admin_ids: Filter by admin ID of user that made the API request
    :type admin_ids: List[str]
    :param user_agent: Filter by user agent string for API request. This will filter by a complete or partial match.
    :type user_agent: str

    """
    return web.Response(status=200)
