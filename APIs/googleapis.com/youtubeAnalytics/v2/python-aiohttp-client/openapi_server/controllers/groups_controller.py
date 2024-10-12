from typing import List, Dict
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.group import Group
from openapi_server.models.list_groups_response import ListGroupsResponse
from openapi_server import util


async def youtube_analytics_groups_delete(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, id=None, on_behalf_of_content_owner=None) -> web.Response:
    """youtube_analytics_groups_delete

    Deletes a group.

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
    :param id: The &#x60;id&#x60; parameter specifies the YouTube group ID of the group that is being deleted.
    :type id: str
    :param on_behalf_of_content_owner: This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
    :type on_behalf_of_content_owner: str

    """
    return web.Response(status=200)


async def youtube_analytics_groups_insert(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, on_behalf_of_content_owner=None, body=None) -> web.Response:
    """youtube_analytics_groups_insert

    Creates a group.

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
    :param on_behalf_of_content_owner: This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
    :type on_behalf_of_content_owner: str
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def youtube_analytics_groups_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, id=None, mine=None, on_behalf_of_content_owner=None, page_token=None) -> web.Response:
    """youtube_analytics_groups_list

    Returns a collection of groups that match the API request parameters. For example, you can retrieve all groups that the authenticated user owns, or you can retrieve one or more groups by their unique IDs.

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
    :param id: The &#x60;id&#x60; parameter specifies a comma-separated list of the YouTube group ID(s) for the resource(s) that are being retrieved. Each group must be owned by the authenticated user. In a &#x60;group&#x60; resource, the &#x60;id&#x60; property specifies the group&#39;s YouTube group ID. Note that if you do not specify a value for the &#x60;id&#x60; parameter, then you must set the &#x60;mine&#x60; parameter to &#x60;true&#x60;.
    :type id: str
    :param mine: This parameter can only be used in a properly authorized request. Set this parameter&#39;s value to true to retrieve all groups owned by the authenticated user.
    :type mine: bool
    :param on_behalf_of_content_owner: This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
    :type on_behalf_of_content_owner: str
    :param page_token: The &#x60;pageToken&#x60; parameter identifies a specific page in the result set that should be returned. In an API response, the &#x60;nextPageToken&#x60; property identifies the next page that can be retrieved.
    :type page_token: str

    """
    return web.Response(status=200)


async def youtube_analytics_groups_update(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, on_behalf_of_content_owner=None, body=None) -> web.Response:
    """youtube_analytics_groups_update

    Modifies a group. For example, you could change a group&#39;s title.

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
    :param on_behalf_of_content_owner: This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
    :type on_behalf_of_content_owner: str
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)
