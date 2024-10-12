from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_organization_api_requests(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, admin_id=None, path=None, method=None, response_code=None, source_ip=None) -> web.Response:
    """List the API requests made by an organization

    List the API requests made by an organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param admin_id: Filter the results by the ID of the admin who made the API requests
    :type admin_id: str
    :param path: Filter the results by the path of the API requests
    :type path: str
    :param method: Filter the results by the method of the API requests (must be &#39;GET&#39;, &#39;PUT&#39;, &#39;POST&#39; or &#39;DELETE&#39;)
    :type method: str
    :param response_code: Filter the results by the response code of the API requests
    :type response_code: int
    :param source_ip: Filter the results by the IP address of the originating API request
    :type source_ip: str

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return an aggregated overview of API requests data

    Return an aggregated overview of API requests data

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float

    """
    return web.Response(status=200)
