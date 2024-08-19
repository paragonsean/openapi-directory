from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment_thread import CommentThread
from openapi_server.models.comment_thread_list_response import CommentThreadListResponse
from openapi_server import util


async def youtube_comment_threads_insert(request: web.Request, part, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """youtube_comment_threads_insert

    Inserts a new resource into this collection.

    :param part: The *part* parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.
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
    :param body: 
    :type body: dict | bytes

    """
    body = CommentThread.from_dict(body)
    return web.Response(status=200)


async def youtube_comment_threads_list(request: web.Request, part, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, all_threads_related_to_channel_id=None, channel_id=None, id=None, max_results=None, moderation_status=None, order=None, page_token=None, search_terms=None, text_format=None, video_id=None) -> web.Response:
    """youtube_comment_threads_list

    Retrieves a list of resources, possibly filtered.

    :param part: The *part* parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include.
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
    :param all_threads_related_to_channel_id: Returns the comment threads of all videos of the channel and the channel comments as well.
    :type all_threads_related_to_channel_id: str
    :param channel_id: Returns the comment threads for all the channel comments (ie does not include comments left on videos).
    :type channel_id: str
    :param id: Returns the comment threads with the given IDs for Stubby or Apiary.
    :type id: List[str]
    :param max_results: The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
    :type max_results: int
    :param moderation_status: Limits the returned comment threads to those with the specified moderation status. Not compatible with the &#39;id&#39; filter. Valid values: published, heldForReview, likelySpam.
    :type moderation_status: str
    :param order: 
    :type order: str
    :param page_token: The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
    :type page_token: str
    :param search_terms: Limits the returned comment threads to those matching the specified key words. Not compatible with the &#39;id&#39; filter.
    :type search_terms: str
    :param text_format: The requested text format for the returned comments.
    :type text_format: str
    :param video_id: Returns the comment threads of the specified video.
    :type video_id: str

    """
    return web.Response(status=200)
