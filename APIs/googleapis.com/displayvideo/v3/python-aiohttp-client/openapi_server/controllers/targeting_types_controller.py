from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_targeting_options_response import ListTargetingOptionsResponse
from openapi_server.models.search_targeting_options_request import SearchTargetingOptionsRequest
from openapi_server.models.search_targeting_options_response import SearchTargetingOptionsResponse
from openapi_server.models.targeting_option import TargetingOption
from openapi_server import util


async def displayvideo_targeting_types_targeting_options_get(request: web.Request, targeting_type, targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None) -> web.Response:
    """displayvideo_targeting_types_targeting_options_get

    Gets a single targeting option.

    :param targeting_type: Required. The type of targeting option to retrieve. Accepted values are: * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60;
    :type targeting_type: str
    :param targeting_option_id: Required. The ID of the of targeting option to retrieve.
    :type targeting_option_id: str
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
    :param advertiser_id: Required. The Advertiser this request is being made in the context of.
    :type advertiser_id: str

    """
    return web.Response(status=200)


async def displayvideo_targeting_types_targeting_options_list(request: web.Request, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_targeting_types_targeting_options_list

    Lists targeting options of a given type.

    :param targeting_type: Required. The type of targeting option to be listed. Accepted values are: * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60;
    :type targeting_type: str
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
    :param advertiser_id: Required. The Advertiser this request is being made in the context of.
    :type advertiser_id: str
    :param filter: Allows filtering by targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;OR&#x60; logical operators. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;carrierAndIspDetails.type&#x60; * &#x60;geoRegionDetails.geoRegionType&#x60; * &#x60;targetingOptionId&#x60; Examples: * All &#x60;GEO REGION&#x60; targeting options that belong to sub type &#x60;GEO_REGION_TYPE_COUNTRY&#x60; or &#x60;GEO_REGION_TYPE_STATE&#x60;: &#x60;geoRegionDetails.geoRegionType&#x3D;\&quot;GEO_REGION_TYPE_COUNTRY\&quot; OR geoRegionDetails.geoRegionType&#x3D;\&quot;GEO_REGION_TYPE_STATE\&quot;&#x60; * All &#x60;CARRIER AND ISP&#x60; targeting options that belong to sub type &#x60;CARRIER_AND_ISP_TYPE_CARRIER&#x60;: &#x60;carrierAndIspDetails.type&#x3D;\&quot;CARRIER_AND_ISP_TYPE_CARRIER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;targetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;targetingOptionId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_targeting_types_targeting_options_search(request: web.Request, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_targeting_types_targeting_options_search

    Searches for targeting options of a given type based on the given search terms.

    :param targeting_type: Required. The type of targeting options to retrieve. Accepted values are: * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60;
    :type targeting_type: str
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
    body = SearchTargetingOptionsRequest.from_dict(body)
    return web.Response(status=200)
