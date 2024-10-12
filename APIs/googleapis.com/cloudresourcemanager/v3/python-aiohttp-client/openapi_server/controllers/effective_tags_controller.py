from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_effective_tags_response import ListEffectiveTagsResponse
from openapi_server import util


async def cloudresourcemanager_effective_tags_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, parent=None) -> web.Response:
    """cloudresourcemanager_effective_tags_list

    Return a list of effective tags for the given Google Cloud resource, as specified in &#x60;parent&#x60;.

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
    :param page_size: Optional. The maximum number of effective tags to return in the response. The server allows a maximum of 300 effective tags to return in a single page. If unspecified, the server will use 100 as the default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to &#x60;ListEffectiveTags&#x60; that indicates from where this listing should continue.
    :type page_token: str
    :param parent: Required. The full resource name of a resource for which you want to list the effective tags. E.g. \&quot;//cloudresourcemanager.googleapis.com/projects/123\&quot;
    :type parent: str

    """
    return web.Response(status=200)
