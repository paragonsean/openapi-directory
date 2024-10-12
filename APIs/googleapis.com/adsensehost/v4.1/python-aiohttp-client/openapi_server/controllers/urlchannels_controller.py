from typing import List, Dict
from aiohttp import web

from openapi_server.models.url_channel import UrlChannel
from openapi_server.models.url_channels import UrlChannels
from openapi_server import util


async def adsensehost_urlchannels_delete(request: web.Request, ad_client_id, url_channel_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_urlchannels_delete

    Delete a URL channel from the host AdSense account.

    :param ad_client_id: Ad client from which to delete the URL channel.
    :type ad_client_id: str
    :param url_channel_id: URL channel to delete.
    :type url_channel_id: str
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


async def adsensehost_urlchannels_insert(request: web.Request, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_urlchannels_insert

    Add a new URL channel to the host AdSense account.

    :param ad_client_id: Ad client to which the new URL channel will be added.
    :type ad_client_id: str
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
    body = UrlChannel.from_dict(body)
    return web.Response(status=200)


async def adsensehost_urlchannels_list(request: web.Request, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """adsensehost_urlchannels_list

    List all host URL channels in the host AdSense account.

    :param ad_client_id: Ad client for which to list URL channels.
    :type ad_client_id: str
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
    :param max_results: The maximum number of URL channels to include in the response, used for paging.
    :type max_results: int
    :param page_token: A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)
