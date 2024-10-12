from typing import List, Dict
from aiohttp import web

from openapi_server.models.report import Report
from openapi_server import util


async def adsensehost_reports_generate(request: web.Request, start_date, end_date, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, dimension=None, filter=None, locale=None, max_results=None, metric=None, sort=None, start_index=None) -> web.Response:
    """adsensehost_reports_generate

    Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify \&quot;alt&#x3D;csv\&quot; as a query parameter.

    :param start_date: Start of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive.
    :type start_date: str
    :param end_date: End of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive.
    :type end_date: str
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
    :param dimension: Dimensions to base the report on.
    :type dimension: List[str]
    :param filter: Filters to be run on the report.
    :type filter: List[str]
    :param locale: Optional locale to use for translating report output to a local language. Defaults to \&quot;en_US\&quot; if not specified.
    :type locale: str
    :param max_results: The maximum number of rows of report data to return.
    :type max_results: int
    :param metric: Numeric columns to include in the report.
    :type metric: List[str]
    :param sort: The name of a dimension or metric to sort the resulting report on, optionally prefixed with \&quot;+\&quot; to sort ascending or \&quot;-\&quot; to sort descending. If no prefix is specified, the column is sorted ascending.
    :type sort: List[str]
    :param start_index: Index of the first row of report data to return.
    :type start_index: int

    """
    return web.Response(status=200)
