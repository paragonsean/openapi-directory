from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.compose_request import ComposeRequest
from openapi_server.models.object import Object
from openapi_server.models.objects import Objects
from openapi_server import util


async def storage_objects_compose(request: web.Request, destination_bucket, destination_object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_generation_match=None, if_metageneration_match=None, body=None) -> web.Response:
    """storage_objects_compose

    Concatenates a list of existing objects into a new object in the same bucket.

    :param destination_bucket: Name of the bucket containing the source objects. The destination object is stored in this bucket.
    :type destination_bucket: str
    :param destination_object: Name of the new object.
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value.
    :type if_generation_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param body: 
    :type body: dict | bytes

    """
    body = ComposeRequest.from_dict(body)
    return web.Response(status=200)


async def storage_objects_copy(request: web.Request, source_bucket, source_object, destination_bucket, destination_object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, projection=None, source_generation=None, body=None) -> web.Response:
    """storage_objects_copy

    Copies an object to a destination in the same location. Optionally overrides metadata.

    :param source_bucket: Name of the bucket in which to find the source object.
    :type source_bucket: str
    :param source_object: Name of the source object.
    :type source_object: str
    :param destination_bucket: Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any.
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_generation_match: Makes the operation conditional on whether the destination object&#39;s current generation matches the given value.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the destination object&#39;s current generation does not match the given value.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param if_source_generation_match: Makes the operation conditional on whether the source object&#39;s generation matches the given value.
    :type if_source_generation_match: str
    :param if_source_generation_not_match: Makes the operation conditional on whether the source object&#39;s generation does not match the given value.
    :type if_source_generation_not_match: str
    :param if_source_metageneration_match: Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value.
    :type if_source_metageneration_match: str
    :param if_source_metageneration_not_match: Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value.
    :type if_source_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    :type projection: str
    :param source_generation: If present, selects a specific revision of the source object (as opposed to the latest version, the default).
    :type source_generation: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_delete(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None) -> web.Response:
    """storage_objects_delete

    Deletes data blobs and associated metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

    :param bucket: Name of the bucket in which the object resides.
    :type bucket: str
    :param object: Name of the object.
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param generation: If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str

    """
    return web.Response(status=200)


async def storage_objects_get(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None) -> web.Response:
    """storage_objects_get

    Retrieves objects or their associated metadata.

    :param bucket: Name of the bucket in which the object resides.
    :type bucket: str
    :param object: Name of the object.
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s generation matches the given value.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s generation does not match the given value.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str

    """
    return web.Response(status=200)


async def storage_objects_insert(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, name=None, projection=None, body=None) -> web.Response:
    """storage_objects_insert

    Stores new data blobs and associated metadata.

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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param name: Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any.
    :type name: str
    :param projection: Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    :type projection: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_list(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, delimiter=None, max_results=None, page_token=None, prefix=None, projection=None, versions=None) -> web.Response:
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param delimiter: Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    :type delimiter: str
    :param max_results: Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: Filter results to objects whose names begin with this prefix.
    :type prefix: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param versions: If true, lists all versions of a file as distinct results.
    :type versions: bool

    """
    return web.Response(status=200)


async def storage_objects_patch(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, body=None) -> web.Response:
    """storage_objects_patch

    Updates a data blob&#39;s associated metadata. This method supports patch semantics.

    :param bucket: Name of the bucket in which the object resides.
    :type bucket: str
    :param object: Name of the object.
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_update(request: web.Request, bucket, object, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, projection=None, body=None) -> web.Response:
    """storage_objects_update

    Updates a data blob&#39;s associated metadata.

    :param bucket: Name of the bucket in which the object resides.
    :type bucket: str
    :param object: Name of the object.
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param generation: If present, selects a specific revision of this object (as opposed to the latest version, the default).
    :type generation: str
    :param if_generation_match: Makes the operation conditional on whether the object&#39;s current generation matches the given value.
    :type if_generation_match: str
    :param if_generation_not_match: Makes the operation conditional on whether the object&#39;s current generation does not match the given value.
    :type if_generation_not_match: str
    :param if_metageneration_match: Makes the operation conditional on whether the object&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str
    :param projection: Set of properties to return. Defaults to full.
    :type projection: str
    :param body: 
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def storage_objects_watch_all(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, delimiter=None, max_results=None, page_token=None, prefix=None, projection=None, versions=None, body=None) -> web.Response:
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param delimiter: Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    :type delimiter: str
    :param max_results: Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: Filter results to objects whose names begin with this prefix.
    :type prefix: str
    :param projection: Set of properties to return. Defaults to noAcl.
    :type projection: str
    :param versions: If true, lists all versions of a file as distinct results.
    :type versions: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
