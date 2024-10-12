from typing import List, Dict
from aiohttp import web

from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets import Buckets
from openapi_server import util


async def storage_buckets_delete(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None) -> web.Response:
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str

    """
    return web.Response(status=200)


async def storage_buckets_get(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None) -> web.Response:
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str

    """
    return web.Response(status=200)


async def storage_buckets_insert(request: web.Request, project, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, projection=None, body=None) -> web.Response:
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.
    :type projection: str
    :param body: 
    :type body: dict | bytes

    """
    body = Bucket.from_dict(body)
    return web.Response(status=200)


async def storage_buckets_list(request: web.Request, project, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None, projection=None) -> web.Response:
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: Maximum number of buckets to return.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str

    """
    return web.Response(status=200)


async def storage_buckets_patch(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, body=None) -> web.Response:
    """storage_buckets_patch

    Updates a bucket. This method supports patch semantics.

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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param body: 
    :type body: dict | bytes

    """
    body = Bucket.from_dict(body)
    return web.Response(status=200)


async def storage_buckets_update(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, body=None) -> web.Response:
    """storage_buckets_update

    Updates a bucket.

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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_metageneration_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param body: 
    :type body: dict | bytes

    """
    body = Bucket.from_dict(body)
    return web.Response(status=200)
