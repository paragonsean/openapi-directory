from typing import List, Dict
from aiohttp import web

from openapi_server.models.advertiser_landing_pages_list_response import AdvertiserLandingPagesListResponse
from openapi_server.models.landing_page import LandingPage
from openapi_server import util


async def dfareporting_advertiser_landing_pages_get(request: web.Request, profile_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dfareporting_advertiser_landing_pages_get

    Gets one landing page by ID.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param id: Landing page ID.
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


async def dfareporting_advertiser_landing_pages_insert(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_advertiser_landing_pages_insert

    Inserts a new landing page.

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
    body = LandingPage.from_dict(body)
    return web.Response(status=200)


async def dfareporting_advertiser_landing_pages_list(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_ids=None, archived=None, campaign_ids=None, ids=None, max_results=None, page_token=None, search_string=None, sort_field=None, sort_order=None, subaccount_id=None) -> web.Response:
    """dfareporting_advertiser_landing_pages_list

    Retrieves a list of landing pages.

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
    :param advertiser_ids: Select only landing pages that belong to these advertisers.
    :type advertiser_ids: List[str]
    :param archived: Select only archived landing pages. Don&#39;t set this field to select both archived and non-archived landing pages.
    :type archived: bool
    :param campaign_ids: Select only landing pages that are associated with these campaigns.
    :type campaign_ids: List[str]
    :param ids: Select only landing pages with these IDs.
    :type ids: List[str]
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param page_token: Value of the nextPageToken from the previous result page.
    :type page_token: str
    :param search_string: Allows searching for landing pages by name or ID. Wildcards (*) are allowed. For example, \&quot;landingpage*2017\&quot; will return landing pages with names like \&quot;landingpage July 2017\&quot;, \&quot;landingpage March 2017\&quot;, or simply \&quot;landingpage 2017\&quot;. Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \&quot;landingpage\&quot; will match campaigns with name \&quot;my landingpage\&quot;, \&quot;landingpage 2015\&quot;, or simply \&quot;landingpage\&quot;.
    :type search_string: str
    :param sort_field: Field by which to sort the list.
    :type sort_field: str
    :param sort_order: Order of sorted results.
    :type sort_order: str
    :param subaccount_id: Select only landing pages that belong to this subaccount.
    :type subaccount_id: str

    """
    return web.Response(status=200)


async def dfareporting_advertiser_landing_pages_patch(request: web.Request, profile_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_advertiser_landing_pages_patch

    Updates an existing advertiser landing page. This method supports patch semantics.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param id: LandingPage ID.
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
    body = LandingPage.from_dict(body)
    return web.Response(status=200)


async def dfareporting_advertiser_landing_pages_update(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_advertiser_landing_pages_update

    Updates an existing landing page.

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
    body = LandingPage.from_dict(body)
    return web.Response(status=200)
