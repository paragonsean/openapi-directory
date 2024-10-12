from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_list_response import ActivityListResponse
from openapi_server import util


async def youtube_activities_list(request: web.Request, part, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, channel_id=None, home=None, max_results=None, mine=None, page_token=None, published_after=None, published_before=None, region_code=None) -> web.Response:
    """youtube_activities_list

    Retrieves a list of resources, possibly filtered.

    :param part: The *part* parameter specifies a comma-separated list of one or more activity resource properties that the API response will include. If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in an activity resource, the snippet property contains other properties that identify the type of activity, a display title for the activity, and so forth. If you set *part&#x3D;snippet*, the API response will also contain all of those nested properties.
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
    :param channel_id: 
    :type channel_id: str
    :param home: 
    :type home: bool
    :param max_results: The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
    :type max_results: int
    :param mine: 
    :type mine: bool
    :param page_token: The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
    :type page_token: str
    :param published_after: 
    :type published_after: str
    :param published_before: 
    :type published_before: str
    :param region_code: 
    :type region_code: str

    """
    return web.Response(status=200)
