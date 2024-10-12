from typing import List, Dict
from aiohttp import web

from openapi_server.models.campaign_creative_association import CampaignCreativeAssociation
from openapi_server.models.campaign_creative_associations_list_response import CampaignCreativeAssociationsListResponse
from openapi_server import util


async def dfareporting_campaign_creative_associations_insert(request: web.Request, profile_id, campaign_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dfareporting_campaign_creative_associations_insert

    Associates a creative with the specified campaign. This method creates a default ad with dimensions matching the creative in the campaign if such a default ad does not exist already.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param campaign_id: Campaign ID in this association.
    :type campaign_id: str
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
    body = CampaignCreativeAssociation.from_dict(body)
    return web.Response(status=200)


async def dfareporting_campaign_creative_associations_list(request: web.Request, profile_id, campaign_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None, sort_order=None) -> web.Response:
    """dfareporting_campaign_creative_associations_list

    Retrieves the list of creative IDs associated with the specified campaign. This method supports paging.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param campaign_id: Campaign ID in this association.
    :type campaign_id: str
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
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param page_token: Value of the nextPageToken from the previous result page.
    :type page_token: str
    :param sort_order: Order of sorted results.
    :type sort_order: str

    """
    return web.Response(status=200)
