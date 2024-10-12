from typing import List, Dict
from aiohttp import web

from openapi_server.models.folder import Folder
from openapi_server.models.folders import Folders
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def storage_folders_delete(request: web.Request, bucket, folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None) -> web.Response:
    """storage_folders_delete

    Permanently deletes a folder. Only applicable to buckets with hierarchical namespace enabled.

    :param bucket: Name of the bucket in which the folder resides.
    :type bucket: str
    :param folder: Name of a folder.
    :type folder: str
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
    :param if_metageneration_match: If set, only deletes the folder if its metageneration matches this value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: If set, only deletes the folder if its metageneration does not match this value.
    :type if_metageneration_not_match: str

    """
    return web.Response(status=200)


async def storage_folders_get(request: web.Request, bucket, folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_metageneration_match=None, if_metageneration_not_match=None) -> web.Response:
    """storage_folders_get

    Returns metadata for the specified folder. Only applicable to buckets with hierarchical namespace enabled.

    :param bucket: Name of the bucket in which the folder resides.
    :type bucket: str
    :param folder: Name of a folder.
    :type folder: str
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
    :param if_metageneration_match: Makes the return of the folder metadata conditional on whether the folder&#39;s current metageneration matches the given value.
    :type if_metageneration_match: str
    :param if_metageneration_not_match: Makes the return of the folder metadata conditional on whether the folder&#39;s current metageneration does not match the given value.
    :type if_metageneration_not_match: str

    """
    return web.Response(status=200)


async def storage_folders_insert(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, recursive=None, body=None) -> web.Response:
    """storage_folders_insert

    Creates a new folder. Only applicable to buckets with hierarchical namespace enabled.

    :param bucket: Name of the bucket in which the folder resides.
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
    :param recursive: If true, any parent folder which doesn’t exist will be created automatically.
    :type recursive: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Folder.from_dict(body)
    return web.Response(status=200)


async def storage_folders_list(request: web.Request, bucket, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, delimiter=None, end_offset=None, page_size=None, page_token=None, prefix=None, start_offset=None) -> web.Response:
    """storage_folders_list

    Retrieves a list of folders matching the criteria. Only applicable to buckets with hierarchical namespace enabled.

    :param bucket: Name of the bucket in which to look for folders.
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
    :param delimiter: Returns results in a directory-like mode. The only supported value is &#39;/&#39;. If set, items will only contain folders that either exactly match the prefix, or are one level below the prefix.
    :type delimiter: str
    :param end_offset: Filter results to folders whose names are lexicographically before endOffset. If startOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive).
    :type end_offset: str
    :param page_size: Maximum number of items to return in a single page of responses.
    :type page_size: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param prefix: Filter results to folders whose paths begin with this prefix. If set, the value must either be an empty string or end with a &#39;/&#39;.
    :type prefix: str
    :param start_offset: Filter results to folders whose names are lexicographically equal to or after startOffset. If endOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive).
    :type start_offset: str

    """
    return web.Response(status=200)


async def storage_folders_rename(request: web.Request, bucket, source_folder, destination_folder, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None) -> web.Response:
    """storage_folders_rename

    Renames a source folder to a destination folder. Only applicable to buckets with hierarchical namespace enabled.

    :param bucket: Name of the bucket in which the folders are in.
    :type bucket: str
    :param source_folder: Name of the source folder.
    :type source_folder: str
    :param destination_folder: Name of the destination folder.
    :type destination_folder: str
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
    :param if_source_metageneration_match: Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value.
    :type if_source_metageneration_match: str
    :param if_source_metageneration_not_match: Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value.
    :type if_source_metageneration_not_match: str

    """
    return web.Response(status=200)
