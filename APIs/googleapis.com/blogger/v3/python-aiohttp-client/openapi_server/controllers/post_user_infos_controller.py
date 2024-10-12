from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_user_info import PostUserInfo
from openapi_server.models.post_user_infos_list import PostUserInfosList
from openapi_server import util


async def blogger_post_user_infos_get(request: web.Request, user_id, blog_id, post_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_comments=None) -> web.Response:
    """blogger_post_user_infos_get

    Gets one post and user info pair, by post_id and user_id.

    :param user_id: 
    :type user_id: str
    :param blog_id: 
    :type blog_id: str
    :param post_id: 
    :type post_id: str
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
    :param max_comments: 
    :type max_comments: int

    """
    return web.Response(status=200)


async def blogger_post_user_infos_list(request: web.Request, user_id, blog_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_date=None, fetch_bodies=None, labels=None, max_results=None, order_by=None, page_token=None, start_date=None, status=None, view=None) -> web.Response:
    """blogger_post_user_infos_list

    Lists post and user info pairs.

    :param user_id: 
    :type user_id: str
    :param blog_id: 
    :type blog_id: str
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
    :param end_date: 
    :type end_date: str
    :param fetch_bodies: 
    :type fetch_bodies: bool
    :param labels: 
    :type labels: str
    :param max_results: 
    :type max_results: int
    :param order_by: 
    :type order_by: str
    :param page_token: 
    :type page_token: str
    :param start_date: 
    :type start_date: str
    :param status: 
    :type status: List[str]
    :param view: 
    :type view: str

    """
    return web.Response(status=200)
