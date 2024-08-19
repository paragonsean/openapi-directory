from typing import List, Dict
from aiohttp import web

from openapi_server.models.member_list_response import MemberListResponse
from openapi_server import util


async def youtube_members_list(request: web.Request, part, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter_by_member_channel_id=None, has_access_to_level=None, max_results=None, mode=None, page_token=None) -> web.Response:
    """youtube_members_list

    Retrieves a list of members that match the request criteria for a channel.

    :param part: The *part* parameter specifies the member resource parts that the API response will include. Set the parameter value to snippet.
    :type part: List[str]
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
    :param filter_by_member_channel_id: Comma separated list of channel IDs. Only data about members that are part of this list will be included in the response.
    :type filter_by_member_channel_id: str
    :param has_access_to_level: Filter members in the results set to the ones that have access to a level.
    :type has_access_to_level: str
    :param max_results: The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
    :type max_results: int
    :param mode: Parameter that specifies which channel members to return.
    :type mode: str
    :param page_token: The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
    :type page_token: str

    """
    return web.Response(status=200)
