from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_customer_index_stats_response import GetCustomerIndexStatsResponse
from openapi_server.models.get_customer_query_stats_response import GetCustomerQueryStatsResponse
from openapi_server.models.get_customer_search_application_stats_response import GetCustomerSearchApplicationStatsResponse
from openapi_server.models.get_customer_session_stats_response import GetCustomerSessionStatsResponse
from openapi_server.models.get_customer_user_stats_response import GetCustomerUserStatsResponse
from openapi_server.models.get_data_source_index_stats_response import GetDataSourceIndexStatsResponse
from openapi_server.models.get_search_application_query_stats_response import GetSearchApplicationQueryStatsResponse
from openapi_server.models.get_search_application_session_stats_response import GetSearchApplicationSessionStatsResponse
from openapi_server.models.get_search_application_user_stats_response import GetSearchApplicationUserStatsResponse
from openapi_server import util


async def cloudsearch_stats_get_index(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_get_index

    Gets indexed item statistics aggreggated across all data sources. This API only returns statistics for previous dates; it doesn&#39;t return statistics for the current day. **Note:** This API requires a standard end user account to execute.

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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_get_query(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_get_query

    Get the query statistics for customer. **Note:** This API requires a standard end user account to execute.

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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_get_searchapplication(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_date_day=None, end_date_month=None, end_date_year=None, start_date_day=None, start_date_month=None, start_date_year=None) -> web.Response:
    """cloudsearch_stats_get_searchapplication

    Get search application stats for customer. **Note:** This API requires a standard end user account to execute.

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
    :param end_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type end_date_day: int
    :param end_date_month: Month of date. Must be from 1 to 12.
    :type end_date_month: int
    :param end_date_year: Year of date. Must be from 1 to 9999.
    :type end_date_year: int
    :param start_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type start_date_day: int
    :param start_date_month: Month of date. Must be from 1 to 12.
    :type start_date_month: int
    :param start_date_year: Year of date. Must be from 1 to 9999.
    :type start_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_get_session(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_get_session

    Get the # of search sessions, % of successful sessions with a click query statistics for customer. **Note:** This API requires a standard end user account to execute.

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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_get_user(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_get_user

    Get the users statistics for customer. **Note:** This API requires a standard end user account to execute.

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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_index_datasources_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_index_datasources_get

    Gets indexed item statistics for a single data source. **Note:** This API requires a standard end user account to execute.

    :param name: The resource id of the data source to retrieve statistics for, in the following format: \&quot;datasources/{source_id}\&quot;
    :type name: str
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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_query_searchapplications_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_query_searchapplications_get

    Get the query statistics for search application. **Note:** This API requires a standard end user account to execute.

    :param name: The resource id of the search application query stats, in the following format: searchapplications/{application_id}
    :type name: str
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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_session_searchapplications_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_session_searchapplications_get

    Get the # of search sessions, % of successful sessions with a click query statistics for search application. **Note:** This API requires a standard end user account to execute.

    :param name: The resource id of the search application session stats, in the following format: searchapplications/{application_id}
    :type name: str
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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)


async def cloudsearch_stats_user_searchapplications_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, from_date_day=None, from_date_month=None, from_date_year=None, to_date_day=None, to_date_month=None, to_date_year=None) -> web.Response:
    """cloudsearch_stats_user_searchapplications_get

    Get the users statistics for search application. **Note:** This API requires a standard end user account to execute.

    :param name: The resource id of the search application session stats, in the following format: searchapplications/{application_id}
    :type name: str
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
    :param from_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type from_date_day: int
    :param from_date_month: Month of date. Must be from 1 to 12.
    :type from_date_month: int
    :param from_date_year: Year of date. Must be from 1 to 9999.
    :type from_date_year: int
    :param to_date_day: Day of month. Must be from 1 to 31 and valid for the year and month.
    :type to_date_day: int
    :param to_date_month: Month of date. Must be from 1 to 12.
    :type to_date_month: int
    :param to_date_year: Year of date. Must be from 1 to 9999.
    :type to_date_year: int

    """
    return web.Response(status=200)
