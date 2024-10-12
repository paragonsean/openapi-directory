from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_calls_settings import BusinessCallsSettings
from openapi_server.models.list_business_calls_insights_response import ListBusinessCallsInsightsResponse
from openapi_server import util


async def mybusinessbusinesscalls_locations_businesscallsinsights_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """mybusinessbusinesscalls_locations_businesscallsinsights_list

    Returns insights for Business calls for a location.

    :param parent: Required. The parent location to fetch calls insights for. Format: locations/{location_id}
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
    :param filter: Optional. A filter constraining the calls insights to return. The response includes only entries that match the filter. If the MetricType is not provided, AGGREGATE_COUNT is returned. If no end_date is provided, the last date for which data is available is used. If no start_date is provided, we will default to the first date for which data is available, which is currently 6 months. If start_date is before the date when data is available, data is returned starting from the date when it is available. At this time we support following filters. 1. start_date&#x3D;\&quot;DATE\&quot; where date is in YYYY-MM-DD format. 2. end_date&#x3D;\&quot;DATE\&quot; where date is in YYYY-MM-DD format. 3. metric_type&#x3D;XYZ where XYZ is a valid MetricType. 4. Conjunctions(AND) of all of the above. e.g., \&quot;start_date&#x3D;2021-08-01 AND end_date&#x3D;2021-08-10 AND metric_type&#x3D;AGGREGATE_COUNT\&quot; The AGGREGATE_COUNT metric_type ignores the DD part of the date.
    :type filter: str
    :param page_size: Optional. The maximum number of BusinessCallsInsights to return. If unspecified, at most 20 will be returned. Some of the metric_types(e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the page_size is ignored.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListBusinessCallsInsights&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListBusinessCallsInsights&#x60; must match the call that provided the page token. Some of the metric_types (e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the pake_token is ignored.
    :type page_token: str

    """
    return web.Response(status=200)


async def mybusinessbusinesscalls_locations_get_businesscallssettings(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """mybusinessbusinesscalls_locations_get_businesscallssettings

    Returns the Business calls settings resource for the given location.

    :param name: Required. The BusinessCallsSettings to get. The &#x60;name&#x60; field is used to identify the business call settings to get. Format: locations/{location_id}/businesscallssettings.
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

    """
    return web.Response(status=200)


async def mybusinessbusinesscalls_locations_update_businesscallssettings(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """mybusinessbusinesscalls_locations_update_businesscallssettings

    Updates the Business call settings for the specified location.

    :param name: Required. The resource name of the calls settings. Format: locations/{location}/businesscallssettings
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
    :param update_mask: Required. The list of fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = BusinessCallsSettings.from_dict(body)
    return web.Response(status=200)
