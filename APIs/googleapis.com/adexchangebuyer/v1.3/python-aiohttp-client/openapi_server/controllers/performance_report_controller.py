from typing import List, Dict
from aiohttp import web

from openapi_server.models.performance_report_list import PerformanceReportList
from openapi_server import util


async def adexchangebuyer_performance_report_list(request: web.Request, account_id, end_date_time, start_date_time, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """adexchangebuyer_performance_report_list

    Retrieves the authenticated user&#39;s list of performance metrics.

    :param account_id: The account id to get the reports.
    :type account_id: str
    :param end_date_time: The end time of the report in ISO 8601 timestamp format using UTC.
    :type end_date_time: str
    :param start_date_time: The start time of the report in ISO 8601 timestamp format using UTC.
    :type start_date_time: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: Maximum number of entries returned on one result page. If not set, the default is 100. Optional.
    :type max_results: int
    :param page_token: A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. Optional.
    :type page_token: str

    """
    return web.Response(status=200)
