from typing import List, Dict
from aiohttp import web

from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets import Buckets
from openapi_server.models.policy import Policy
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server import util


async def storage_buckets_delete(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, user_project=None) -> web.Response:
    """storage_buckets_delete

    Permanently deletes an empty bucket.

    :param bucket: Name of a bucket.
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
    :param if_metageneration_match: If set, only deletes the bucket if its metageneration matches this value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: If set, only deletes the bucket if its metageneration does not match this value.
    :type if_metageneration_not_match: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_buckets_get(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, user_project=None) -> web.Response:
    """storage_buckets_get

    Returns metadata for the specified bucket.

    :param bucket: Name of a bucket.
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
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_buckets_get_iam_policy(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, options_requested_policy_version=None, user_project=None) -> web.Response:
    """storage_buckets_get_iam_policy

    Returns an IAM policy for the specified bucket.

    :param bucket: Name of a bucket.
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
    :param options_requested_policy_version: The IAM policy format version to be returned. If the optionsRequestedPolicyVersion is for an older version that doesn&#39;t support part of the requested IAM policy, the request fails.
    :type options_requested_policy_version: int
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_buckets_insert(request: web.Request, project, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, enable_object_retention=None, predefined_acl=None, predefined_default_object_acl=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_buckets_insert

    Creates a new bucket.

    :param project: A valid API project identifier.
    :type project: str
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
    :param enable_object_retention: When set to true, object retention is enabled for this bucket.
    :type enable_object_retention: bool
    :param predefined_acl: Apply a predefined set of access controls to this bucket.
    :type predefined_acl: str
    :param predefined_default_object_acl: Apply a predefined set of default object access controls to this bucket.
    :type predefined_default_object_acl: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Bucket.from_dict(body)
    return web.Response(status=200)


async def storage_buckets_list(request: web.Request, project, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, max_results=None, page_token=None, prefix=None, projection=None, user_project=None) -> web.Response:
    """storage_buckets_list

    Retrieves a list of buckets for a given project.

    :param project: A valid API project identifier.
    :type project: str
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
    :param max_results: Maximum number of buckets to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: Filter results to buckets whose names begin with this prefix.
    :type prefix: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param user_project: The project to be billed for this request.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_buckets_lock_retention_policy(request: web.Request, bucket, if_metageneration_match, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_buckets_lock_retention_policy

    Locks retention policy on a bucket.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param if_metageneration_match: Makes the operation conditional on whether bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
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
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_buckets_patch(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, predefined_acl=None, predefined_default_object_acl=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_buckets_patch

    Patches a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

    :param bucket: Name of a bucket.
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
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param predefined_acl: Apply a predefined set of access controls to this bucket.
    :type predefined_acl: str
    :param predefined_default_object_acl: Apply a predefined set of default object access controls to this bucket.
    :type predefined_default_object_acl: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Bucket.from_dict(body)
    return web.Response(status=200)


async def storage_buckets_set_iam_policy(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None, body=None) -> web.Response:
    """storage_buckets_set_iam_policy

    Updates an IAM policy for the specified bucket.

    :param bucket: Name of a bucket.
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
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Policy.from_dict(body)
    return web.Response(status=200)


async def storage_buckets_test_iam_permissions(request: web.Request, bucket, permissions, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_buckets_test_iam_permissions

    Tests a set of permissions on the given bucket to see which, if any, are held by the caller.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param permissions: Permissions to test.
    :type permissions: List[str]
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
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_buckets_update(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, predefined_acl=None, predefined_default_object_acl=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_buckets_update

    Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

    :param bucket: Name of a bucket.
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
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param predefined_acl: Apply a predefined set of access controls to this bucket.
    :type predefined_acl: str
    :param predefined_default_object_acl: Apply a predefined set of default object access controls to this bucket.
    :type predefined_default_object_acl: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Bucket.from_dict(body)
    return web.Response(status=200)
