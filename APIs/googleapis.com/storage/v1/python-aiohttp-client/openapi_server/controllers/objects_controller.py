from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_restore_objects_request import BulkRestoreObjectsRequest
from openapi_server.models.channel import Channel
from openapi_server.models.compose_request import ComposeRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server.models.object import Object
from openapi_server.models.objects import Objects
from openapi_server.models.policy import Policy
from openapi_server.models.rewrite_response import RewriteResponse
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server import util


async def storage_objects_bulk_restore(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, body=None) -> web.Response:
    """storage_objects_bulk_restore

    Initiates a long-running bulk restore operation on the specified bucket.

    :param bucket: Name of the bucket in which the object resides.
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
    body = BulkRestoreObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def storage_objects_compose(request: web.Request, destination_bucket, destination_object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, destination_predefined_acl=None, if_generation_match=None, if_metageneration_match=None, kms_key_name=None, user_project=None, body=None) -> web.Response:
    """storage_objects_compose

    Concatenates a list of existing objects into a new object in the same bucket.

    :param destination_bucket: Name of the bucket containing the source objects. The destination object is stored in this bucket.
    :type destination_bucket: str
    :param destination_object: Name of the new object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type destination_object: str
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
    :param destination_predefined_acl: Apply a predefined set of access controls to the destination object.
    :type destination_predefined_acl: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param kms_key_name: Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any.
    :type kms_key_name: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = ComposeRequest.from_dict(body)
    return web.Response(status=200)


async def storage_objects_copy(request: web.Request, source_bucket, source_object, destination_bucket, destination_object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, destination_kms_key_name=None, destination_predefined_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, projection=None, source_generation=None, user_project=None, body=None) -> web.Response:
    """storage_objects_copy

    Copies a source object to a destination object. Optionally overrides metadata.

    :param source_bucket: Name of the bucket in which to find the source object.
    :type source_bucket: str
    :param source_object: Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type source_object: str
    :param destination_bucket: Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any.For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type destination_bucket: str
    :param destination_object: Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any.
    :type destination_object: str
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
    :param destination_kms_key_name: Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any.
    :type destination_kms_key_name: str
    :param destination_predefined_acl: Apply a predefined set of access controls to the destination object.
    :type destination_predefined_acl: str
    :param if_generation_match: Makes the operation conditional on whether the destination object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the destination object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param if_source_generation_match: Makes the operation conditional on whether the source object&#39;s current generation matches the given value.
    :type if_source_generation_match: str
    :param if_source_generation_not_match: Makes the operation conditional on whether the source object&#39;s current generation does not match the given value.
    :type if_source_generation_not_match: str
    :param if_source_metageneration_match: Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value.
    :type if_source_metageneration_match: str
    :param if_source_metageneration_not_match: Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value.
    :type if_source_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    :type projection: str
    :param source_generation: If present, selects a specific revision of the source object (as opposed to the latest version, the default).
    :type source_generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_delete(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, user_project=None) -> web.Response:
    """storage_objects_delete

    Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

    :param bucket: Name of the bucket in which the object resides.
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
    :param generation: If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_objects_get(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, soft_deleted=None, user_project=None) -> web.Response:
    """storage_objects_get

    Retrieves an object or its metadata.

    :param bucket: Name of the bucket in which the object resides.
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
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param soft_deleted: If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete.
    :type soft_deleted: bool
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_objects_get_iam_policy(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None) -> web.Response:
    """storage_objects_get_iam_policy

    Returns an IAM policy for the specified object.

    :param bucket: Name of the bucket in which the object resides.
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


async def storage_objects_insert(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, content_encoding=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, kms_key_name=None, name=None, predefined_acl=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_objects_insert

    Stores a new object and metadata.

    :param bucket: Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any.
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
    :param content_encoding: If set, sets the contentEncoding property of the final object to this value. Setting this parameter is equivalent to setting the contentEncoding metadata property. This can be useful when uploading an object with uploadType&#x3D;media to indicate the encoding of the content being uploaded.
    :type content_encoding: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param kms_key_name: Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any.
    :type kms_key_name: str
    :param name: Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type name: str
    :param predefined_acl: Apply a predefined set of access controls to this object.
    :type predefined_acl: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_list(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, delimiter=None, end_offset=None, include_folders_as_prefixes=None, include_trailing_delimiter=None, match_glob=None, max_results=None, page_token=None, prefix=None, projection=None, soft_deleted=None, start_offset=None, user_project=None, versions=None) -> web.Response:
    """storage_objects_list

    Retrieves a list of objects matching the criteria.

    :param bucket: Name of the bucket in which to look for objects.
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
    :param delimiter: Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    :type delimiter: str
    :param end_offset: Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    :type end_offset: str
    :param include_folders_as_prefixes: Only applicable if delimiter is set to &#39;/&#39;. If true, will also include folders and managed folders (besides objects) in the returned prefixes.
    :type include_folders_as_prefixes: bool
    :param include_trailing_delimiter: If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.
    :type include_trailing_delimiter: bool
    :param match_glob: Filter results to objects and prefixes that match this glob pattern.
    :type match_glob: str
    :param max_results: Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: Filter results to objects whose names begin with this prefix.
    :type prefix: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param soft_deleted: If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete.
    :type soft_deleted: bool
    :param start_offset: Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    :type start_offset: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param versions: If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.
    :type versions: bool

    """
    return web.Response(status=200)


async def storage_objects_patch(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, override_unlocked_retention=None, predefined_acl=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_objects_patch

    Patches an object&#39;s metadata.

    :param bucket: Name of the bucket in which the object resides.
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
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param override_unlocked_retention: Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked.
    :type override_unlocked_retention: bool
    :param predefined_acl: Apply a predefined set of access controls to this object.
    :type predefined_acl: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request, for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_restore(request: web.Request, bucket, object, generation, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, copy_source_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_objects_restore

    Restores a soft-deleted object.

    :param bucket: Name of the bucket in which the object resides.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.
    :type object: str
    :param generation: Selects a specific revision of this object.
    :type generation: str
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
    :param copy_source_acl: If true, copies the source object&#39;s ACL; otherwise, uses the bucket&#39;s default object ACL. The default is false.
    :type copy_source_acl: bool
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s one live generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether none of the object&#39;s live generations match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s one live metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether none of the object&#39;s live metagenerations match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_rewrite(request: web.Request, source_bucket, source_object, destination_bucket, destination_object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, destination_kms_key_name=None, destination_predefined_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, max_bytes_rewritten_per_call=None, projection=None, rewrite_token=None, source_generation=None, user_project=None, body=None) -> web.Response:
    """storage_objects_rewrite

    Rewrites a source object to a destination object. Optionally overrides metadata.

    :param source_bucket: Name of the bucket in which to find the source object.
    :type source_bucket: str
    :param source_object: Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type source_object: str
    :param destination_bucket: Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any.
    :type destination_bucket: str
    :param destination_object: Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type destination_object: str
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
    :param destination_kms_key_name: Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any.
    :type destination_kms_key_name: str
    :param destination_predefined_acl: Apply a predefined set of access controls to the destination object.
    :type destination_predefined_acl: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param if_source_generation_match: Makes the operation conditional on whether the source object&#39;s current generation matches the given value.
    :type if_source_generation_match: str
    :param if_source_generation_not_match: Makes the operation conditional on whether the source object&#39;s current generation does not match the given value.
    :type if_source_generation_not_match: str
    :param if_source_metageneration_match: Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value.
    :type if_source_metageneration_match: str
    :param if_source_metageneration_not_match: Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value.
    :type if_source_metageneration_not_match: str
    :param max_bytes_rewritten_per_call: The maximum number of bytes that will be rewritten per rewrite request. Most callers shouldn&#39;t need to specify this parameter - it is primarily in place to support testing. If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only applies to requests where the source and destination span locations and/or storage classes. Finally, this value must not change across rewrite calls else you&#39;ll get an error that the rewriteToken is invalid.
    :type max_bytes_rewritten_per_call: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    :type projection: str
    :param rewrite_token: Include this field (from the previous rewrite response) on each rewrite request after the first one, until the rewrite response &#39;done&#39; flag is true. Calls that provide a rewriteToken can omit all other request fields, but if included those fields must match the values provided in the first rewrite request.
    :type rewrite_token: str
    :param source_generation: If present, selects a specific revision of the source object (as opposed to the latest version, the default).
    :type source_generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_set_iam_policy(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None, body=None) -> web.Response:
    """storage_objects_set_iam_policy

    Updates an IAM policy for the specified object.

    :param bucket: Name of the bucket in which the object resides.
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
    body = Policy.from_dict(body)
    return web.Response(status=200)


async def storage_objects_test_iam_permissions(request: web.Request, bucket, object, permissions, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, user_project=None) -> web.Response:
    """storage_objects_test_iam_permissions

    Tests a set of permissions on the given object to see which, if any, are held by the caller.

    :param bucket: Name of the bucket in which the object resides.
    :type bucket: str
    :param object: Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    :type object: str
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
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_objects_update(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, override_unlocked_retention=None, predefined_acl=None, projection=None, user_project=None, body=None) -> web.Response:
    """storage_objects_update

    Updates an object&#39;s metadata.

    :param bucket: Name of the bucket in which the object resides.
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
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param override_unlocked_retention: Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked.
    :type override_unlocked_retention: bool
    :param predefined_acl: Apply a predefined set of access controls to this object.
    :type predefined_acl: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_watch_all(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, delimiter=None, end_offset=None, include_trailing_delimiter=None, max_results=None, page_token=None, prefix=None, projection=None, start_offset=None, user_project=None, versions=None, body=None) -> web.Response:
    """storage_objects_watch_all

    Watch for changes on all objects in a bucket.

    :param bucket: Name of the bucket in which to look for objects.
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
    :param delimiter: Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    :type delimiter: str
    :param end_offset: Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    :type end_offset: str
    :param include_trailing_delimiter: If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.
    :type include_trailing_delimiter: bool
    :param max_results: Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: Filter results to objects whose names begin with this prefix.
    :type prefix: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param start_offset: Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    :type start_offset: str
    :param user_project: The project to be billed for this request. Required for Requester Pays buckets.
    :type user_project: str
    :param versions: If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.
    :type versions: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
