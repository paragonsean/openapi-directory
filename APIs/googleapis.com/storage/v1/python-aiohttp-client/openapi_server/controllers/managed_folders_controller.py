from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_folder import ManagedFolder
from openapi_server.models.managed_folders import ManagedFolders
from openapi_server.models.policy import Policy
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server import util


async def storage_managed_folders_delete(request: web.Request, bucket, managed_folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None) -> web.Response:
    """storage_managed_folders_delete

    Permanently deletes a managed folder.

    :param bucket: Name of the bucket containing the managed folder.
    :type bucket: str
    :param managed_folder: The managed folder name/path.
    :type managed_folder: str
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
    :param if_metageneration_match: If set, only deletes the managed folder if its metageneration matches this value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: If set, only deletes the managed folder if its metageneration does not match this value.
    :type if_metageneration_not_match: str

    """
    return web.Response(status=200)


async def storage_managed_folders_get(request: web.Request, bucket, managed_folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None) -> web.Response:
    """storage_managed_folders_get

    Returns metadata of the specified managed folder.

    :param bucket: Name of the bucket containing the managed folder.
    :type bucket: str
    :param managed_folder: The managed folder name/path.
    :type managed_folder: str
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
    :param if_metageneration_match: Makes the return of the managed folder metadata conditional on whether the managed folder&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the managed folder metadata conditional on whether the managed folder&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str

    """
    return web.Response(status=200)


async def storage_managed_folders_get_iam_policy(request: web.Request, bucket, managed_folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, options_requested_policy_version=None, user_project=None) -> web.Response:
    """storage_managed_folders_get_iam_policy

    Returns an IAM policy for the specified managed folder.

    :param bucket: Name of the bucket containing the managed folder.
    :type bucket: str
    :param managed_folder: The managed folder name/path.
    :type managed_folder: str
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


async def storage_managed_folders_insert(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, body=None) -> web.Response:
    """storage_managed_folders_insert

    Creates a new managed folder.

    :param bucket: Name of the bucket containing the managed folder.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ManagedFolder.from_dict(body)
    return web.Response(status=200)


async def storage_managed_folders_list(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, page_size=None, page_token=None, prefix=None) -> web.Response:
    """storage_managed_folders_list

    Lists managed folders in the given bucket.

    :param bucket: Name of the bucket containing the managed folder.
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
    :param page_size: Maximum number of items to return in a single page of responses.
    :type page_size: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: The managed folder name/path prefix to filter the output list of results.
    :type prefix: str

    """
    return web.Response(status=200)


async def storage_managed_folders_set_iam_policy(request: web.Request, bucket, managed_folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None, body=None) -> web.Response:
    """storage_managed_folders_set_iam_policy

    Updates an IAM policy for the specified managed folder.

    :param bucket: Name of the bucket containing the managed folder.
    :type bucket: str
    :param managed_folder: The managed folder name/path.
    :type managed_folder: str
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


async def storage_managed_folders_test_iam_permissions(request: web.Request, bucket, managed_folder, permissions, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_managed_folders_test_iam_permissions

    Tests a set of permissions on the given managed folder to see which, if any, are held by the caller.

    :param bucket: Name of the bucket containing the managed folder.
    :type bucket: str
    :param managed_folder: The managed folder name/path.
    :type managed_folder: str
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
