from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_list import CustomList
from openapi_server.models.list_custom_lists_response import ListCustomListsResponse
from openapi_server import util


async def displayvideo_custom_lists_get(request: web.Request, custom_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None) -> web.Response:
    """displayvideo_custom_lists_get

    Gets a custom list.

    :param custom_list_id: Required. The ID of the custom list to fetch.
    :type custom_list_id: str
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
    :param advertiser_id: The ID of the DV360 advertiser that has access to the fetched custom lists.
    :type advertiser_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_lists_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_custom_lists_list

    Lists custom lists. The order is defined by the order_by parameter.

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
    :param advertiser_id: The ID of the DV360 advertiser that has access to the fetched custom lists.
    :type advertiser_id: str
    :param filter: Allows filtering by custom list fields. Supported syntax: * Filter expressions for custom lists can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;displayName&#x60; Examples: * All custom lists for which the display name contains \&quot;Google\&quot;: &#x60;displayName:\&quot;Google\&quot;&#x60;. The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;customListId&#x60; (default) * &#x60;displayName&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCustomLists&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)
