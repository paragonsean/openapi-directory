from typing import List, Dict
from aiohttp import web

from openapi_server.models.object_access_control import ObjectAccessControl
from openapi_server.models.object_access_controls import ObjectAccessControls
from openapi_server import util


async def storage_object_access_controls_delete(request: web.Request, bucket, object, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None) -> web.Response:
    """storage_object_access_controls_delete

    Permanently deletes the ACL entry for the specified entity on the specified object.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_object_access_controls_get(request: web.Request, bucket, object, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None) -> web.Response:
    """storage_object_access_controls_get

    Returns the ACL entry for the specified entity on the specified object.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_object_access_controls_insert(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None, body=None) -> web.Response:
    """storage_object_access_controls_insert

    Creates a new ACL entry on the specified object.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = ObjectAccessControl.from_dict(body)
    return web.Response(status=200)


async def storage_object_access_controls_list(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None) -> web.Response:
    """storage_object_access_controls_list

    Retrieves ACL entries on the specified object.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_object_access_controls_patch(request: web.Request, bucket, object, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None, body=None) -> web.Response:
    """storage_object_access_controls_patch

    Patches an ACL entry on the specified object.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = ObjectAccessControl.from_dict(body)
    return web.Response(status=200)


async def storage_object_access_controls_update(request: web.Request, bucket, object, entity, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None, body=None) -> web.Response:
    """storage_object_access_controls_update

    Updates an ACL entry on the specified object.

    :param bucket: Name of a bucket.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = ObjectAccessControl.from_dict(body)
    return web.Response(status=200)
