from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_kms_inventory_v1_search_protected_resources_response import GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse
from openapi_server import util


async def kmsinventory_organizations_protected_resources_search(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, crypto_key=None, page_size=None, page_token=None, resource_types=None) -> web.Response:
    """kmsinventory_organizations_protected_resources_search

    Returns metadata about the resources protected by the given Cloud KMS CryptoKey in the given Cloud organization.

    :param scope: Required. Resource name of the organization. Example: organizations/123
    :type scope: str
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
    :param crypto_key: Required. The resource name of the CryptoKey.
    :type crypto_key: str
    :param page_size: The maximum number of resources to return. The service may return fewer than this value. If unspecified, at most 500 resources will be returned. The maximum value is 500; values above 500 will be coerced to 500.
    :type page_size: int
    :param page_token: A page token, received from a previous KeyTrackingService.SearchProtectedResources call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to KeyTrackingService.SearchProtectedResources must match the call that provided the page token.
    :type page_token: str
    :param resource_types: Optional. A list of resource types that this request searches for. If empty, it will search all the [trackable resource types](https://cloud.google.com/kms/docs/view-key-usage#tracked-resource-types). Regular expressions are also supported. For example: * &#x60;compute.googleapis.com.*&#x60; snapshots resources whose type starts with &#x60;compute.googleapis.com&#x60;. * &#x60;.*Image&#x60; snapshots resources whose type ends with &#x60;Image&#x60;. * &#x60;.*Image.*&#x60; snapshots resources whose type contains &#x60;Image&#x60;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported resource type, an INVALID_ARGUMENT error will be returned.
    :type resource_types: List[str]

    """
    return web.Response(status=200)
