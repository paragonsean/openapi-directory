from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def storage_buckets_operations_cancel(request: web.Request, bucket, operation_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None) -> web.Response:
    """storage_buckets_operations_cancel

    Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed.

    :param bucket: The parent bucket of the operation resource.
    :type bucket: str
    :param operation_id: The ID of the operation resource.
    :type operation_id: str
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
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def storage_buckets_operations_get(request: web.Request, bucket, operation_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None) -> web.Response:
    """storage_buckets_operations_get

    Gets the latest state of a long-running operation.

    :param bucket: The parent bucket of the operation resource.
    :type bucket: str
    :param operation_id: The ID of the operation resource.
    :type operation_id: str
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
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def storage_buckets_operations_list(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """storage_buckets_operations_list

    Lists operations that match the specified filter in the request.

    :param bucket: Name of the bucket in which to look for operations.
    :type bucket: str
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
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param filter: A filter to narrow down results to a preferred subset. The filtering language is documented in more detail in [AIP-160](https://google.aip.dev/160).
    :type filter: str
    :param page_size: Maximum number of items to return in a single page of responses. Fewer total results may be returned than requested. The service uses this parameter or 100 items, whichever is smaller.
    :type page_size: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str

    """
    return web.Response(status=200)
