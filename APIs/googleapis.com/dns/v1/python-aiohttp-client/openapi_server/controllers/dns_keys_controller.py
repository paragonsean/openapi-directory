from typing import List, Dict
from aiohttp import web

from openapi_server.models.dns_key import DnsKey
from openapi_server.models.dns_keys_list_response import DnsKeysListResponse
from openapi_server import util


async def dns_dns_keys_get(request: web.Request, project, managed_zone, dns_key_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, client_operation_id=None, digest_type=None) -> web.Response:
    """dns_dns_keys_get

    Fetches the representation of an existing DnsKey.

    :param project: Identifies the project addressed by this request.
    :type project: str
    :param managed_zone: Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
    :type managed_zone: str
    :param dns_key_id: The identifier of the requested DnsKey.
    :type dns_key_id: str
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
    :param client_operation_id: For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    :type client_operation_id: str
    :param digest_type: An optional comma-separated list of digest types to compute and display for key signing keys. If omitted, the recommended digest type is computed and displayed.
    :type digest_type: str

    """
    return web.Response(status=200)


async def dns_dns_keys_list(request: web.Request, project, managed_zone, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, digest_type=None, max_results=None, page_token=None) -> web.Response:
    """dns_dns_keys_list

    Enumerates DnsKeys to a ResourceRecordSet collection.

    :param project: Identifies the project addressed by this request.
    :type project: str
    :param managed_zone: Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
    :type managed_zone: str
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
    :param digest_type: An optional comma-separated list of digest types to compute and display for key signing keys. If omitted, the recommended digest type is computed and displayed.
    :type digest_type: str
    :param max_results: Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.
    :type max_results: int
    :param page_token: Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.
    :type page_token: str

    """
    return web.Response(status=200)
