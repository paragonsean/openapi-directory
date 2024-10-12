from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_tag_bindings_response import ListTagBindingsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.tag_binding import TagBinding
from openapi_server import util


async def cloudresourcemanager_tag_bindings_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, validate_only=None, body=None) -> web.Response:
    """cloudresourcemanager_tag_bindings_create

    Creates a TagBinding between a TagValue and a Google Cloud resource.

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
    :param validate_only: Optional. Set to true to perform the validations necessary for creating the resource, but not actually perform the action.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = TagBinding.from_dict(body)
    return web.Response(status=200)


async def cloudresourcemanager_tag_bindings_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, parent=None) -> web.Response:
    """cloudresourcemanager_tag_bindings_list

    Lists the TagBindings for the given Google Cloud resource, as specified with &#x60;parent&#x60;. NOTE: The &#x60;parent&#x60; field is expected to be a full resource name: https://cloud.google.com/apis/design/resource_names#full_resource_name

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
    :param page_size: Optional. The maximum number of TagBindings to return in the response. The server allows a maximum of 300 TagBindings to return. If unspecified, the server will use 100 as the default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to &#x60;ListTagBindings&#x60; that indicates where this listing should continue from.
    :type page_token: str
    :param parent: Required. The full resource name of a resource for which you want to list existing TagBindings. E.g. \&quot;//cloudresourcemanager.googleapis.com/projects/123\&quot;
    :type parent: str

    """
    return web.Response(status=200)
