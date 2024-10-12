from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_platforms_response import ListPlatformsResponse
from openapi_server.models.list_releases_response import ListReleasesResponse
from openapi_server.models.list_versions_response import ListVersionsResponse
from openapi_server import util


async def versionhistory_platforms_channels_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """versionhistory_platforms_channels_list

    Returns list of channels that are available for a given platform.

    :param parent: Required. The platform, which owns this collection of channels. Format: {product}/platforms/{platform}
    :type parent: str
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
    :param page_size: Optional. Optional limit on the number of channels to include in the response. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListChannels&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def versionhistory_platforms_channels_versions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """versionhistory_platforms_channels_versions_list

    Returns list of version for the given platform/channel.

    :param parent: Required. The channel, which owns this collection of versions. Format: {product}/platforms/{platform}/channels/{channel}
    :type parent: str
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
    :param filter: Optional. Filter string. Format is a comma separated list of All comma separated filter clauses are conjoined with a logical \&quot;and\&quot;. Valid field_names are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;platform\&quot;, and \&quot;channel\&quot;. Valid operators are \&quot;&lt;\&quot;, \&quot;&lt;&#x3D;\&quot;, \&quot;&#x3D;\&quot;, \&quot;&gt;&#x3D;\&quot;, and \&quot;&gt;\&quot;. Channel comparison is done by distance from stable. Ex) stable &lt; beta, beta &lt; dev, canary &lt; canary_asan. Version comparison is done numerically. If version is not entirely written, the version will be appended with 0 in missing fields. Ex) version &gt; 80 becoms version &gt; 80.0.0.0 Name and platform are filtered by string comparison. Ex) \&quot;...?filter&#x3D;channel&lt;&#x3D;beta, version &gt;&#x3D; 80 Ex) \&quot;...?filter&#x3D;version &gt; 80, version &lt; 81
    :type filter: str
    :param order_by: Optional. Ordering string. Valid order_by strings are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;platform\&quot;, and \&quot;channel\&quot;. Optionally, you can append \&quot; desc\&quot; or \&quot; asc\&quot; to specify the sorting order. Multiple order_by strings can be used in a comma separated list. Ordering by channel will sort by distance from the stable channel (not alphabetically). A list of channels sorted in this order is: stable, beta, dev, canary, and canary_asan. Sorting by name may cause unexpected behaviour as it is a naive string sort. For example, 1.0.0.8 will be before 1.0.0.10 in descending order. If order_by is not specified the response will be sorted by version in descending order. Ex) \&quot;...?order_by&#x3D;version asc\&quot; Ex) \&quot;...?order_by&#x3D;platform desc, channel, version\&quot;
    :type order_by: str
    :param page_size: Optional. Optional limit on the number of versions to include in the response. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListVersions&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def versionhistory_platforms_channels_versions_releases_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """versionhistory_platforms_channels_versions_releases_list

    Returns list of releases of the given version.

    :param parent: Required. The version, which owns this collection of releases. Format: {product}/platforms/{platform}/channels/{channel}/versions/{version}
    :type parent: str
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
    :param filter: Optional. Filter string. Format is a comma separated list of All comma separated filter clauses are conjoined with a logical \&quot;and\&quot;. Valid field_names are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;platform\&quot;, \&quot;channel\&quot;, \&quot;fraction\&quot; \&quot;starttime\&quot;, and \&quot;endtime\&quot;. Valid operators are \&quot;&lt;\&quot;, \&quot;&lt;&#x3D;\&quot;, \&quot;&#x3D;\&quot;, \&quot;&gt;&#x3D;\&quot;, and \&quot;&gt;\&quot;. Channel comparison is done by distance from stable. must be a valid channel when filtering by channel. Ex) stable &lt; beta, beta &lt; dev, canary &lt; canary_asan. Version comparison is done numerically. Ex) 1.0.0.8 &lt; 1.0.0.10. If version is not entirely written, the version will be appended with 0 for the missing fields. Ex) version &gt; 80 becoms version &gt; 80.0.0.0 When filtering by starttime or endtime, string must be in RFC 3339 date string format. Name and platform are filtered by string comparison. Ex) \&quot;...?filter&#x3D;channel&lt;&#x3D;beta, version &gt;&#x3D; 80 Ex) \&quot;...?filter&#x3D;version &gt; 80, version &lt; 81 Ex) \&quot;...?filter&#x3D;starttime&gt;2020-01-01T00:00:00Z
    :type filter: str
    :param order_by: Optional. Ordering string. Valid order_by strings are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;starttime\&quot;, \&quot;endtime\&quot;, \&quot;platform\&quot;, \&quot;channel\&quot;, and \&quot;fraction\&quot;. Optionally, you can append \&quot;desc\&quot; or \&quot;asc\&quot; to specify the sorting order. Multiple order_by strings can be used in a comma separated list. Ordering by channel will sort by distance from the stable channel (not alphabetically). A list of channels sorted in this order is: stable, beta, dev, canary, and canary_asan. Sorting by name may cause unexpected behaviour as it is a naive string sort. For example, 1.0.0.8 will be before 1.0.0.10 in descending order. If order_by is not specified the response will be sorted by starttime in descending order. Ex) \&quot;...?order_by&#x3D;starttime asc\&quot; Ex) \&quot;...?order_by&#x3D;platform desc, channel, startime desc\&quot;
    :type order_by: str
    :param page_size: Optional. Optional limit on the number of releases to include in the response. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListReleases&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def versionhistory_platforms_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """versionhistory_platforms_list

    Returns list of platforms that are available for a given product. The resource \&quot;product\&quot; has no resource name in its name.

    :param parent: Required. The product, which owns this collection of platforms. Format: {product}
    :type parent: str
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
    :param page_size: Optional. Optional limit on the number of channels to include in the response. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListChannels&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)
