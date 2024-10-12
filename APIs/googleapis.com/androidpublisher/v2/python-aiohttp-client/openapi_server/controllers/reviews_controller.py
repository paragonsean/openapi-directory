from typing import List, Dict
from aiohttp import web

from openapi_server.models.review import Review
from openapi_server.models.reviews_list_response import ReviewsListResponse
from openapi_server.models.reviews_reply_request import ReviewsReplyRequest
from openapi_server.models.reviews_reply_response import ReviewsReplyResponse
from openapi_server import util


async def androidpublisher_reviews_get(request: web.Request, package_name, review_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, translation_language=None) -> web.Response:
    """androidpublisher_reviews_get

    Returns a single review.

    :param package_name: Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param review_id: 
    :type review_id: str
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
    :param translation_language: 
    :type translation_language: str

    """
    return web.Response(status=200)


async def androidpublisher_reviews_list(request: web.Request, package_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, start_index=None, token=None, translation_language=None) -> web.Response:
    """androidpublisher_reviews_list

    Returns a list of reviews. Only reviews from last week will be returned.

    :param package_name: Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
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
    :param max_results: 
    :type max_results: int
    :param start_index: 
    :type start_index: int
    :param token: 
    :type token: str
    :param translation_language: 
    :type translation_language: str

    """
    return web.Response(status=200)


async def androidpublisher_reviews_reply(request: web.Request, package_name, review_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_reviews_reply

    Reply to a single review, or update an existing reply.

    :param package_name: Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param review_id: 
    :type review_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ReviewsReplyRequest.from_dict(body)
    return web.Response(status=200)
