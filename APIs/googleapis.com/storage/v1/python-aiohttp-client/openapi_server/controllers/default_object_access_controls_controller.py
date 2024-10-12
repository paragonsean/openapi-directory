from typing import List, Dict
from aiohttp import web

from openapi_server.models.object_access_control import ObjectAccessControl
from openapi_server.models.object_access_controls import ObjectAccessControls
from openapi_server import util


async def storage_default_object_access_controls_delete(request: web.Request, bucket, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_default_object_access_controls_delete

    Permanently deletes the default object ACL entry for the specified entity on the specified bucket.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param entity: The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    :type entity: str
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


async def storage_default_object_access_controls_get(request: web.Request, bucket, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_default_object_access_controls_get

    Returns the default object ACL entry for the specified entity on the specified bucket.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param entity: The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    :type entity: str
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


async def storage_default_object_access_controls_insert(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None, body=None) -> web.Response:
    """storage_default_object_access_controls_insert

    Creates a new default object ACL entry on the specified bucket.

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
    body = ObjectAccessControl.from_dict(body)
    return web.Response(status=200)


async def storage_default_object_access_controls_list(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None, user_project=None) -> web.Response:
    """storage_default_object_access_controls_list

    Retrieves default object ACL entries on the specified bucket.

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
    :param if_metageneration_match: If present, only return default ACL listing if the bucket&#39;s current metageneration matches this value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: If present, only return default ACL listing if the bucket&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_default_object_access_controls_patch(request: web.Request, bucket, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None, body=None) -> web.Response:
    """storage_default_object_access_controls_patch

    Patches a default object ACL entry on the specified bucket.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param entity: The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    :type entity: str
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
    body = ObjectAccessControl.from_dict(body)
    return web.Response(status=200)


async def storage_default_object_access_controls_update(request: web.Request, bucket, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None, body=None) -> web.Response:
    """storage_default_object_access_controls_update

    Updates a default object ACL entry on the specified bucket.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param entity: The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    :type entity: str
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
    body = ObjectAccessControl.from_dict(body)
    return web.Response(status=200)
