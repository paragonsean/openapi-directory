from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_multi_daily_metrics_time_series_response import FetchMultiDailyMetricsTimeSeriesResponse
from openapi_server.models.get_daily_metrics_time_series_response import GetDailyMetricsTimeSeriesResponse
from openapi_server.models.list_search_keyword_impressions_monthly_response import ListSearchKeywordImpressionsMonthlyResponse
from openapi_server import util


async def businessprofileperformance_locations_fetch_multi_daily_metrics_time_series(request: web.Request, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, daily_metrics=None, daily_range_end_date_day=None, daily_range_end_date_month=None, daily_range_end_date_year=None, daily_range_start_date_day=None, daily_range_start_date_month=None, daily_range_start_date_year=None) -> web.Response:
    """businessprofileperformance_locations_fetch_multi_daily_metrics_time_series

     Returns the values for each date from a given time range and optionally the sub entity type, where applicable, that are associated with the specific daily metrics. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345:fetchMultiDailyMetricsTimeSeries?dailyMetrics&#x3D;WEBSITE_CLICKS&amp;dailyMetrics&#x3D;CALL_CLICKS&amp;daily_range.start_date.year&#x3D;2022&amp;daily_range.start_date.month&#x3D;1&amp;daily_range.start_date.day&#x3D;1&amp;daily_range.end_date.year&#x3D;2022&amp;daily_range.end_date.month&#x3D;3&amp;daily_range.end_date.day&#x3D;31&#x60;

    :param location: Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
    :type location: str
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
    :param daily_metrics: Required. The metrics to retrieve time series for.
    :type daily_metrics: List[str]
    :param daily_range_end_date_day: Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant.
    :type daily_range_end_date_day: int
    :param daily_range_end_date_month: Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    :type daily_range_end_date_month: int
    :param daily_range_end_date_year: Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    :type daily_range_end_date_year: int
    :param daily_range_start_date_day: Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant.
    :type daily_range_start_date_day: int
    :param daily_range_start_date_month: Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    :type daily_range_start_date_month: int
    :param daily_range_start_date_year: Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    :type daily_range_start_date_year: int

    """
    return web.Response(status=200)


async def businessprofileperformance_locations_get_daily_metrics_time_series(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, daily_metric=None, daily_range_end_date_day=None, daily_range_end_date_month=None, daily_range_end_date_year=None, daily_range_start_date_day=None, daily_range_start_date_month=None, daily_range_start_date_year=None, daily_sub_entity_type_day_of_week=None, daily_sub_entity_type_time_of_day_hours=None, daily_sub_entity_type_time_of_day_minutes=None, daily_sub_entity_type_time_of_day_nanos=None, daily_sub_entity_type_time_of_day_seconds=None) -> web.Response:
    """businessprofileperformance_locations_get_daily_metrics_time_series

     Returns the values for each date from a given time range that are associated with the specific daily metric. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345:getDailyMetricsTimeSeries?dailyMetric&#x3D;WEBSITE_CLICKS&amp;daily_range.start_date.year&#x3D;2022&amp;daily_range.start_date.month&#x3D;1&amp;daily_range.start_date.day&#x3D;1&amp;daily_range.end_date.year&#x3D;2022&amp;daily_range.end_date.month&#x3D;3&amp;daily_range.end_date.day&#x3D;31&#x60;

    :param name: Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
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
    :param daily_metric: Required. The metric to retrieve time series.
    :type daily_metric: str
    :param daily_range_end_date_day: Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant.
    :type daily_range_end_date_day: int
    :param daily_range_end_date_month: Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    :type daily_range_end_date_month: int
    :param daily_range_end_date_year: Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    :type daily_range_end_date_year: int
    :param daily_range_start_date_day: Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant.
    :type daily_range_start_date_day: int
    :param daily_range_start_date_month: Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    :type daily_range_start_date_month: int
    :param daily_range_start_date_year: Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    :type daily_range_start_date_year: int
    :param daily_sub_entity_type_day_of_week: Represents the day of the week. Eg: MONDAY. Currently supported DailyMetrics &#x3D; NONE.
    :type daily_sub_entity_type_day_of_week: str
    :param daily_sub_entity_type_time_of_day_hours: Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time.
    :type daily_sub_entity_type_time_of_day_hours: int
    :param daily_sub_entity_type_time_of_day_minutes: Minutes of hour of day. Must be from 0 to 59.
    :type daily_sub_entity_type_time_of_day_minutes: int
    :param daily_sub_entity_type_time_of_day_nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
    :type daily_sub_entity_type_time_of_day_nanos: int
    :param daily_sub_entity_type_time_of_day_seconds: Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.
    :type daily_sub_entity_type_time_of_day_seconds: int

    """
    return web.Response(status=200)


async def businessprofileperformance_locations_searchkeywords_impressions_monthly_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, monthly_range_end_month_day=None, monthly_range_end_month_month=None, monthly_range_end_month_year=None, monthly_range_start_month_day=None, monthly_range_start_month_month=None, monthly_range_start_month_year=None, page_size=None, page_token=None) -> web.Response:
    """businessprofileperformance_locations_searchkeywords_impressions_monthly_list

    Returns the search keywords used to find a business in search or maps. Each search keyword is accompanied by impressions which are aggregated on a monthly basis. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345/searchkeywords/impressions/monthly?monthly_range.start_month.year&#x3D;2022&amp;monthly_range.start_month.month&#x3D;1&amp;monthly_range.end_month.year&#x3D;2022&amp;monthly_range.end_month.month&#x3D;3&#x60;

    :param parent: Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
    :type parent: str
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
    :param monthly_range_end_month_day: Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant.
    :type monthly_range_end_month_day: int
    :param monthly_range_end_month_month: Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    :type monthly_range_end_month_month: int
    :param monthly_range_end_month_year: Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    :type monthly_range_end_month_year: int
    :param monthly_range_start_month_day: Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant.
    :type monthly_range_start_month_day: int
    :param monthly_range_start_month_month: Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    :type monthly_range_start_month_month: int
    :param monthly_range_start_month_year: Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    :type monthly_range_start_month_year: int
    :param page_size: Optional. The number of results requested. The default page size is 100. Page size can be set to a maximum of 100.
    :type page_size: int
    :param page_token: Optional. A token indicating the next paginated result to be returned.
    :type page_token: str

    """
    return web.Response(status=200)
