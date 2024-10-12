from typing import List, Dict
from aiohttp import web

from openapi_server.models.ad import Ad
from openapi_server.models.ads_list_response import AdsListResponse
from openapi_server import util


async def dfareporting_ads_get(request: web.Request, profile_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dfareporting_ads_get

    Gets one ad by ID.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param id: Ad ID.
    :type id: str
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


async def dfareporting_ads_insert(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_ads_insert

    Inserts a new ad.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
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
    body = Ad.from_dict(body)
    return web.Response(status=200)


async def dfareporting_ads_list(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, active=None, advertiser_id=None, archived=None, audience_segment_ids=None, campaign_ids=None, compatibility=None, creative_ids=None, creative_optimization_configuration_ids=None, dynamic_click_tracker=None, ids=None, landing_page_ids=None, max_results=None, overridden_event_tag_id=None, page_token=None, placement_ids=None, remarketing_list_ids=None, search_string=None, size_ids=None, sort_field=None, sort_order=None, ssl_compliant=None, ssl_required=None, type=None) -> web.Response:
    """dfareporting_ads_list

    Retrieves a list of ads, possibly filtered. This method supports paging.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
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
    :param active: Select only active ads.
    :type active: bool
    :param advertiser_id: Select only ads with this advertiser ID.
    :type advertiser_id: str
    :param archived: Select only archived ads.
    :type archived: bool
    :param audience_segment_ids: Select only ads with these audience segment IDs.
    :type audience_segment_ids: List[str]
    :param campaign_ids: Select only ads with these campaign IDs.
    :type campaign_ids: List[str]
    :param compatibility: Select default ads with the specified compatibility. Applicable when type is AD_SERVING_DEFAULT_AD. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. IN_STREAM_VIDEO refers to rendering an in-stream video ads developed with the VAST standard.
    :type compatibility: str
    :param creative_ids: Select only ads with these creative IDs assigned.
    :type creative_ids: List[str]
    :param creative_optimization_configuration_ids: Select only ads with these creative optimization configuration IDs.
    :type creative_optimization_configuration_ids: List[str]
    :param dynamic_click_tracker: Select only dynamic click trackers. Applicable when type is AD_SERVING_CLICK_TRACKER. If true, select dynamic click trackers. If false, select static click trackers. Leave unset to select both.
    :type dynamic_click_tracker: bool
    :param ids: Select only ads with these IDs.
    :type ids: List[str]
    :param landing_page_ids: Select only ads with these landing page IDs.
    :type landing_page_ids: List[str]
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param overridden_event_tag_id: Select only ads with this event tag override ID.
    :type overridden_event_tag_id: str
    :param page_token: Value of the nextPageToken from the previous result page.
    :type page_token: str
    :param placement_ids: Select only ads with these placement IDs assigned.
    :type placement_ids: List[str]
    :param remarketing_list_ids: Select only ads whose list targeting expression use these remarketing list IDs.
    :type remarketing_list_ids: List[str]
    :param search_string: Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \&quot;ad*2015\&quot; will return objects with names like \&quot;ad June 2015\&quot;, \&quot;ad April 2015\&quot;, or simply \&quot;ad 2015\&quot;. Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \&quot;ad\&quot; will match objects with name \&quot;my ad\&quot;, \&quot;ad 2015\&quot;, or simply \&quot;ad\&quot;.
    :type search_string: str
    :param size_ids: Select only ads with these size IDs.
    :type size_ids: List[str]
    :param sort_field: Field by which to sort the list.
    :type sort_field: str
    :param sort_order: Order of sorted results.
    :type sort_order: str
    :param ssl_compliant: Select only ads that are SSL-compliant.
    :type ssl_compliant: bool
    :param ssl_required: Select only ads that require SSL.
    :type ssl_required: bool
    :param type: Select only ads with these types.
    :type type: List[str]

    """
    return web.Response(status=200)


async def dfareporting_ads_patch(request: web.Request, profile_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_ads_patch

    Updates an existing ad. This method supports patch semantics.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param id: Ad ID.
    :type id: str
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
    body = Ad.from_dict(body)
    return web.Response(status=200)


async def dfareporting_ads_update(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_ads_update

    Updates an existing ad.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
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
    body = Ad.from_dict(body)
    return web.Response(status=200)
