from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversion_list import ConversionList
from openapi_server.models.update_availability_request import UpdateAvailabilityRequest
from openapi_server.models.update_availability_response import UpdateAvailabilityResponse
from openapi_server import util


async def doubleclicksearch_conversion_get(request: web.Request, agency_id, advertiser_id, engine_account_id, end_date, row_count, start_date, start_row, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, ad_group_id=None, ad_id=None, campaign_id=None, criterion_id=None, customer_id=None) -> web.Response:
    """doubleclicksearch_conversion_get

    Retrieves a list of conversions from a DoubleClick Search engine account.

    :param agency_id: Numeric ID of the agency.
    :type agency_id: str
    :param advertiser_id: Numeric ID of the advertiser.
    :type advertiser_id: str
    :param engine_account_id: Numeric ID of the engine account.
    :type engine_account_id: str
    :param end_date: Last date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
    :type end_date: int
    :param row_count: The number of conversions to return per call.
    :type row_count: int
    :param start_date: First date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
    :type start_date: int
    :param start_row: The 0-based starting index for retrieving conversions results.
    :type start_row: int
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
    :param ad_group_id: Numeric ID of the ad group.
    :type ad_group_id: str
    :param ad_id: Numeric ID of the ad.
    :type ad_id: str
    :param campaign_id: Numeric ID of the campaign.
    :type campaign_id: str
    :param criterion_id: Numeric ID of the criterion.
    :type criterion_id: str
    :param customer_id: Customer ID of a client account in the new Search Ads 360 experience.
    :type customer_id: str

    """
    return web.Response(status=200)


async def doubleclicksearch_conversion_get_by_customer_id(request: web.Request, customer_id, end_date, row_count, start_date, start_row, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, ad_group_id=None, ad_id=None, advertiser_id=None, agency_id=None, campaign_id=None, criterion_id=None, engine_account_id=None) -> web.Response:
    """doubleclicksearch_conversion_get_by_customer_id

    Retrieves a list of conversions from a DoubleClick Search engine account.

    :param customer_id: Customer ID of a client account in the new Search Ads 360 experience.
    :type customer_id: str
    :param end_date: Last date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
    :type end_date: int
    :param row_count: The number of conversions to return per call.
    :type row_count: int
    :param start_date: First date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
    :type start_date: int
    :param start_row: The 0-based starting index for retrieving conversions results.
    :type start_row: int
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
    :param ad_group_id: Numeric ID of the ad group.
    :type ad_group_id: str
    :param ad_id: Numeric ID of the ad.
    :type ad_id: str
    :param advertiser_id: Numeric ID of the advertiser.
    :type advertiser_id: str
    :param agency_id: Numeric ID of the agency.
    :type agency_id: str
    :param campaign_id: Numeric ID of the campaign.
    :type campaign_id: str
    :param criterion_id: Numeric ID of the criterion.
    :type criterion_id: str
    :param engine_account_id: Numeric ID of the engine account.
    :type engine_account_id: str

    """
    return web.Response(status=200)


async def doubleclicksearch_conversion_insert(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """doubleclicksearch_conversion_insert

    Inserts a batch of new conversions into DoubleClick Search.

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
    :param body: 
    :type body: dict | bytes

    """
    body = ConversionList.from_dict(body)
    return web.Response(status=200)


async def doubleclicksearch_conversion_update(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """doubleclicksearch_conversion_update

    Updates a batch of conversions in DoubleClick Search.

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
    :param body: 
    :type body: dict | bytes

    """
    body = ConversionList.from_dict(body)
    return web.Response(status=200)


async def doubleclicksearch_conversion_update_availability(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """doubleclicksearch_conversion_update_availability

    Updates the availabilities of a batch of floodlight activities in DoubleClick Search.

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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAvailabilityRequest.from_dict(body)
    return web.Response(status=200)
