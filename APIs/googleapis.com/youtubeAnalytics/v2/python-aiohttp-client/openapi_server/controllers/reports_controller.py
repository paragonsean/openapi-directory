from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_response import QueryResponse
from openapi_server import util


async def youtube_analytics_reports_query(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, currency=None, dimensions=None, end_date=None, filters=None, ids=None, include_historical_channel_data=None, max_results=None, metrics=None, sort=None, start_date=None, start_index=None) -> web.Response:
    """youtube_analytics_reports_query

    Retrieve your YouTube Analytics reports.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param currency: The currency to which financial metrics should be converted. The default is US Dollar (USD). If the result contains no financial metrics, this flag will be ignored. Responds with an error if the specified currency is not recognized.\&quot;, pattern: [A-Z]{3}
    :type currency: str
    :param dimensions: A comma-separated list of YouTube Analytics dimensions, such as &#x60;views&#x60; or &#x60;ageGroup,gender&#x60;. See the [Available Reports](/youtube/analytics/v2/available_reports) document for a list of the reports that you can retrieve and the dimensions used for those reports. Also see the [Dimensions](/youtube/analytics/v2/dimsmets/dims) document for definitions of those dimensions.\&quot; pattern: [0-9a-zA-Z,]+
    :type dimensions: str
    :param end_date: The end date for fetching YouTube Analytics data. The value should be in &#x60;YYYY-MM-DD&#x60; format. required: true, pattern: [0-9]{4}-[0-9]{2}-[0-9]{2}
    :type end_date: str
    :param filters: A list of filters that should be applied when retrieving YouTube Analytics data. The [Available Reports](/youtube/analytics/v2/available_reports) document identifies the dimensions that can be used to filter each report, and the [Dimensions](/youtube/analytics/v2/dimsmets/dims) document defines those dimensions. If a request uses multiple filters, join them together with a semicolon (&#x60;;&#x60;), and the returned result table will satisfy both filters. For example, a filters parameter value of &#x60;video&#x3D;&#x3D;dMH0bHeiRNg;country&#x3D;&#x3D;IT&#x60; restricts the result set to include data for the given video in Italy.\&quot;,
    :type filters: str
    :param ids: Identifies the YouTube channel or content owner for which you are retrieving YouTube Analytics data. - To request data for a YouTube user, set the &#x60;ids&#x60; parameter value to &#x60;channel&#x3D;&#x3D;CHANNEL_ID&#x60;, where &#x60;CHANNEL_ID&#x60; specifies the unique YouTube channel ID. - To request data for a YouTube CMS content owner, set the &#x60;ids&#x60; parameter value to &#x60;contentOwner&#x3D;&#x3D;OWNER_NAME&#x60;, where &#x60;OWNER_NAME&#x60; is the CMS name of the content owner. required: true, pattern: [a-zA-Z]+&#x3D;&#x3D;[a-zA-Z0-9_+-]+
    :type ids: str
    :param include_historical_channel_data: If set to true historical data (i.e. channel data from before the linking of the channel to the content owner) will be retrieved.\&quot;,
    :type include_historical_channel_data: bool
    :param max_results: The maximum number of rows to include in the response.\&quot;, minValue: 1
    :type max_results: int
    :param metrics: A comma-separated list of YouTube Analytics metrics, such as &#x60;views&#x60; or &#x60;likes,dislikes&#x60;. See the [Available Reports](/youtube/analytics/v2/available_reports) document for a list of the reports that you can retrieve and the metrics available in each report, and see the [Metrics](/youtube/analytics/v2/dimsmets/mets) document for definitions of those metrics. required: true, pattern: [0-9a-zA-Z,]+
    :type metrics: str
    :param sort: A comma-separated list of dimensions or metrics that determine the sort order for YouTube Analytics data. By default the sort order is ascending. The &#39;&#x60;-&#x60;&#39; prefix causes descending sort order.\&quot;, pattern: [-0-9a-zA-Z,]+
    :type sort: str
    :param start_date: The start date for fetching YouTube Analytics data. The value should be in &#x60;YYYY-MM-DD&#x60; format. required: true, pattern: \&quot;[0-9]{4}-[0-9]{2}-[0-9]{2}
    :type start_date: str
    :param start_index: An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter (one-based, inclusive).\&quot;, minValue: 1
    :type start_index: int

    """
    return web.Response(status=200)
