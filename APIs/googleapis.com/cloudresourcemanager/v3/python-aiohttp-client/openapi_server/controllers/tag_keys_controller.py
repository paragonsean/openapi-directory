from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_tag_keys_response import ListTagKeysResponse
from openapi_server.models.operation import Operation
from openapi_server.models.tag_key import TagKey
from openapi_server import util


async def cloudresourcemanager_tag_keys_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, validate_only=None, body=None) -> web.Response:
    """cloudresourcemanager_tag_keys_create

    Creates a new TagKey. If another request with the same parameters is sent while the original request is in process, the second request will receive an error. A maximum of 1000 TagKeys can exist under a parent at any given time.

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
    :param validate_only: Optional. Set to true to perform validations necessary for creating the resource, but not actually perform the action.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = TagKey.from_dict(body)
    return web.Response(status=200)


async def cloudresourcemanager_tag_keys_get_namespaced(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None) -> web.Response:
    """cloudresourcemanager_tag_keys_get_namespaced

    Retrieves a TagKey by its namespaced name. This method will return &#x60;PERMISSION_DENIED&#x60; if the key does not exist or the user does not have permission to view it.

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
    :param name: Required. A namespaced tag key name in the format &#x60;{parentId}/{tagKeyShort}&#x60;, such as &#x60;42/foo&#x60; for a key with short name \&quot;foo\&quot; under the organization with ID 42 or &#x60;r2-d2/bar&#x60; for a key with short name \&quot;bar\&quot; under the project &#x60;r2-d2&#x60;.
    :type name: str

    """
    return web.Response(status=200)


async def cloudresourcemanager_tag_keys_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, parent=None) -> web.Response:
    """cloudresourcemanager_tag_keys_list

    Lists all TagKeys for a parent resource.

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
    :param page_size: Optional. The maximum number of TagKeys to return in the response. The server allows a maximum of 300 TagKeys to return. If unspecified, the server will use 100 as the default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to &#x60;ListTagKey&#x60; that indicates where this listing should continue from.
    :type page_token: str
    :param parent: Required. The resource name of the TagKey&#39;s parent. Must be of the form &#x60;organizations/{org_id}&#x60; or &#x60;projects/{project_id}&#x60; or &#x60;projects/{project_number}&#x60;
    :type parent: str

    """
    return web.Response(status=200)
