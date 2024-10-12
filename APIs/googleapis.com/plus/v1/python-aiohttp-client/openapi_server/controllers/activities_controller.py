from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_feed import ActivityFeed
from openapi_server import util


async def plus_activities_get(request: web.Request, activity_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """plus_activities_get

    Shut down. See https://developers.google.com/+/api-shutdown for more details.

    :param activity_id: The ID of the activity to get.
    :type activity_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def plus_activities_list(request: web.Request, user_id, collection, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """plus_activities_list

    Shut down. See https://developers.google.com/+/api-shutdown for more details.

    :param user_id: The ID of the user to get activities for. The special value \&quot;me\&quot; can be used to indicate the authenticated user.
    :type user_id: str
    :param collection: The collection of activities to list.
    :type collection: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: The maximum number of activities to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults.
    :type max_results: int
    :param page_token: The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)


async def plus_activities_search(request: web.Request, query, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, language=None, max_results=None, order_by=None, page_token=None) -> web.Response:
    """plus_activities_search

    Shut down. See https://developers.google.com/+/api-shutdown for more details.

    :param query: Full-text search query string.
    :type query: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param language: Specify the preferred language to search with. See search language codes for available values.
    :type language: str
    :param max_results: The maximum number of activities to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults.
    :type max_results: int
    :param order_by: Specifies how to order search results.
    :type order_by: str
    :param page_token: The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. This token can be of any length.
    :type page_token: str

    """
    return web.Response(status=200)
