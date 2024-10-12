from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_channel import CustomChannel
from openapi_server.models.custom_channels import CustomChannels
from openapi_server import util


async def adsensehost_customchannels_delete(request: web.Request, ad_client_id, custom_channel_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_customchannels_delete

    Delete a specific custom channel from the host AdSense account.

    :param ad_client_id: Ad client from which to delete the custom channel.
    :type ad_client_id: str
    :param custom_channel_id: Custom channel to delete.
    :type custom_channel_id: str
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


async def adsensehost_customchannels_get(request: web.Request, ad_client_id, custom_channel_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_customchannels_get

    Get a specific custom channel from the host AdSense account.

    :param ad_client_id: Ad client from which to get the custom channel.
    :type ad_client_id: str
    :param custom_channel_id: Custom channel to get.
    :type custom_channel_id: str
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


async def adsensehost_customchannels_insert(request: web.Request, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_customchannels_insert

    Add a new custom channel to the host AdSense account.

    :param ad_client_id: Ad client to which the new custom channel will be added.
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
    body = CustomChannel.from_dict(body)
    return web.Response(status=200)


async def adsensehost_customchannels_list(request: web.Request, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """adsensehost_customchannels_list

    List all host custom channels in this AdSense account.

    :param ad_client_id: Ad client for which to list custom channels.
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
    :param max_results: The maximum number of custom channels to include in the response, used for paging.
    :type max_results: int
    :param page_token: A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)


async def adsensehost_customchannels_patch(request: web.Request, ad_client_id, custom_channel_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_customchannels_patch

    Update a custom channel in the host AdSense account. This method supports patch semantics.

    :param ad_client_id: Ad client in which the custom channel will be updated.
    :type ad_client_id: str
    :param custom_channel_id: Custom channel to get.
    :type custom_channel_id: str
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
    body = CustomChannel.from_dict(body)
    return web.Response(status=200)


async def adsensehost_customchannels_update(request: web.Request, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_customchannels_update

    Update a custom channel in the host AdSense account.

    :param ad_client_id: Ad client in which the custom channel will be updated.
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
    body = CustomChannel.from_dict(body)
    return web.Response(status=200)
