from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_list_response import SearchListResponse
from openapi_server import util


async def youtube_search_list(request: web.Request, part, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, channel_id=None, channel_type=None, event_type=None, for_content_owner=None, for_developer=None, for_mine=None, location=None, location_radius=None, max_results=None, on_behalf_of_content_owner=None, order=None, page_token=None, published_after=None, published_before=None, q=None, region_code=None, relevance_language=None, safe_search=None, topic_id=None, type=None, video_caption=None, video_category_id=None, video_definition=None, video_dimension=None, video_duration=None, video_embeddable=None, video_license=None, video_paid_product_placement=None, video_syndicated=None, video_type=None) -> web.Response:
    """youtube_search_list

    Retrieves a list of search resources

    :param part: The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet.
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
    :param channel_id: Filter on resources belonging to this channelId.
    :type channel_id: str
    :param channel_type: Add a filter on the channel search.
    :type channel_type: str
    :param event_type: Filter on the livestream status of the videos.
    :type event_type: str
    :param for_content_owner: Search owned by a content owner.
    :type for_content_owner: bool
    :param for_developer: Restrict the search to only retrieve videos uploaded using the project id of the authenticated user.
    :type for_developer: bool
    :param for_mine: Search for the private videos of the authenticated user.
    :type for_mine: bool
    :param location: Filter on location of the video
    :type location: str
    :param location_radius: Filter on distance from the location (specified above).
    :type location_radius: str
    :param max_results: The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
    :type max_results: int
    :param on_behalf_of_content_owner: *Note:* This parameter is intended exclusively for YouTube content partners. The *onBehalfOfContentOwner* parameter indicates that the request&#39;s authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.
    :type on_behalf_of_content_owner: str
    :param order: Sort order of the results.
    :type order: str
    :param page_token: The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
    :type page_token: str
    :param published_after: Filter on resources published after this date.
    :type published_after: str
    :param published_before: Filter on resources published before this date.
    :type published_before: str
    :param q: Textual search terms to match.
    :type q: str
    :param region_code: Display the content as seen by viewers in this country.
    :type region_code: str
    :param relevance_language: Return results relevant to this language.
    :type relevance_language: str
    :param safe_search: Indicates whether the search results should include restricted content as well as standard content.
    :type safe_search: str
    :param topic_id: Restrict results to a particular topic.
    :type topic_id: str
    :param type: Restrict results to a particular set of resource types from One Platform.
    :type type: List[str]
    :param video_caption: Filter on the presence of captions on the videos.
    :type video_caption: str
    :param video_category_id: Filter on videos in a specific category.
    :type video_category_id: str
    :param video_definition: Filter on the definition of the videos.
    :type video_definition: str
    :param video_dimension: Filter on 3d videos.
    :type video_dimension: str
    :param video_duration: Filter on the duration of the videos.
    :type video_duration: str
    :param video_embeddable: Filter on embeddable videos.
    :type video_embeddable: str
    :param video_license: Filter on the license of the videos.
    :type video_license: str
    :param video_paid_product_placement: 
    :type video_paid_product_placement: str
    :param video_syndicated: Filter on syndicated videos.
    :type video_syndicated: str
    :param video_type: Filter on videos of a specific type.
    :type video_type: str

    """
    return web.Response(status=200)
