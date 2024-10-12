from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.file import File
from openapi_server.models.file_list import FileList
from openapi_server.models.generated_ids import GeneratedIds
from openapi_server.models.label_list import LabelList
from openapi_server.models.modify_labels_request import ModifyLabelsRequest
from openapi_server.models.modify_labels_response import ModifyLabelsResponse
from openapi_server import util


async def drive_files_copy(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, enforce_single_parent=None, ignore_default_visibility=None, include_labels=None, include_permissions_for_view=None, keep_revision_forever=None, ocr_language=None, supports_all_drives=None, supports_team_drives=None, body=None) -> web.Response:
    """drive_files_copy

    Creates a copy of a file and applies any requested updates with patch semantics.

    :param file_id: The ID of the file.
    :type file_id: str
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
    :param enforce_single_parent: Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead.
    :type enforce_single_parent: bool
    :param ignore_default_visibility: Whether to ignore the domain&#39;s default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.
    :type ignore_default_visibility: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param keep_revision_forever: Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
    :type keep_revision_forever: bool
    :param ocr_language: A language hint for OCR processing during image import (ISO 639-1 code).
    :type ocr_language: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, enforce_single_parent=None, ignore_default_visibility=None, include_labels=None, include_permissions_for_view=None, keep_revision_forever=None, ocr_language=None, supports_all_drives=None, supports_team_drives=None, use_content_as_indexable_text=None, body=None) -> web.Response:
    """drive_files_create

     Creates a new file. This method supports an */upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*/*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*/*&#x60; value. The literal &#x60;*/*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads). Apps creating shortcuts with &#x60;files.create&#x60; must specify the MIME type &#x60;application/vnd.google-apps.shortcut&#x60;. Apps should specify a file extension in the &#x60;name&#x60; property when inserting files with the API. For example, an operation to insert a JPEG file should specify something like &#x60;\&quot;name\&quot;: \&quot;cat.jpg\&quot;&#x60; in the metadata. Subsequent &#x60;GET&#x60; requests include the read-only &#x60;fileExtension&#x60; property populated with the extension originally specified in the &#x60;title&#x60; property. When a Google Drive user requests to download a file, or when the file is downloaded through the sync client, Drive builds a full filename (with extension) based on the title. In cases where the extension is missing, Drive attempts to determine the extension based on the file&#39;s MIME type.

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
    :param enforce_single_parent: Deprecated. Creating files in multiple folders is no longer supported.
    :type enforce_single_parent: bool
    :param ignore_default_visibility: Whether to ignore the domain&#39;s default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.
    :type ignore_default_visibility: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param keep_revision_forever: Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
    :type keep_revision_forever: bool
    :param ocr_language: A language hint for OCR processing during image import (ISO 639-1 code).
    :type ocr_language: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param use_content_as_indexable_text: Whether to use the uploaded content as indexable text.
    :type use_content_as_indexable_text: bool
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_delete(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, enforce_single_parent=None, supports_all_drives=None, supports_team_drives=None) -> web.Response:
    """drive_files_delete

    Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive, the user must be an &#x60;organizer&#x60; on the parent folder. If the target is a folder, all descendants owned by the user are also deleted.

    :param file_id: The ID of the file.
    :type file_id: str
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
    :param enforce_single_parent: Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner&#39;s root.
    :type enforce_single_parent: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool

    """
    return web.Response(status=200)


async def drive_files_empty_trash(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, drive_id=None, enforce_single_parent=None) -> web.Response:
    """drive_files_empty_trash

    Permanently deletes all of the user&#39;s trashed files.

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
    :param drive_id: If set, empties the trash of the provided shared drive.
    :type drive_id: str
    :param enforce_single_parent: Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner&#39;s root.
    :type enforce_single_parent: bool

    """
    return web.Response(status=200)


async def drive_files_export(request: web.Request, file_id, mime_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """drive_files_export

    Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.

    :param file_id: The ID of the file.
    :type file_id: str
    :param mime_type: Required. The MIME type of the format requested for this export.
    :type mime_type: str
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

    """
    return web.Response(status=200)


async def drive_files_generate_ids(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, count=None, space=None, type=None) -> web.Response:
    """drive_files_generate_ids

    Generates a set of file IDs which can be provided in create or copy requests.

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
    :param count: The number of IDs to return.
    :type count: int
    :param space: The space in which the IDs can be used to create new files. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. (Default: &#39;drive&#39;)
    :type space: str
    :param type: The type of items which the IDs can be used for. Supported values are &#39;files&#39; and &#39;shortcuts&#39;. Note that &#39;shortcuts&#39; are only supported in the &#x60;drive&#x60; &#39;space&#39;. (Default: &#39;files&#39;)
    :type type: str

    """
    return web.Response(status=200)


async def drive_files_get(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, acknowledge_abuse=None, include_labels=None, include_permissions_for_view=None, supports_all_drives=None, supports_team_drives=None) -> web.Response:
    """drive_files_get

     Gets a file&#39;s metadata or content by ID. If you provide the URL parameter &#x60;alt&#x3D;media&#x60;, then the response includes the file contents in the response body. Downloading content with &#x60;alt&#x3D;media&#x60; only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [&#x60;files.export&#x60;](/drive/api/reference/rest/v3/files/export) instead. For more information, see [Download &amp; export files](/drive/api/guides/manage-downloads).

    :param file_id: The ID of the file.
    :type file_id: str
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
    :param acknowledge_abuse: Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt&#x3D;media.
    :type acknowledge_abuse: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool

    """
    return web.Response(status=200)


async def drive_files_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, corpora=None, corpus=None, drive_id=None, include_items_from_all_drives=None, include_labels=None, include_permissions_for_view=None, include_team_drive_items=None, order_by=None, page_size=None, page_token=None, q=None, spaces=None, supports_all_drives=None, supports_team_drives=None, team_drive_id=None) -> web.Response:
    """drive_files_list

     Lists the user&#39;s files. This method accepts the &#x60;q&#x60; parameter, which is a search query combining one or more search terms. For more information, see the [Search for files &amp; folders](/drive/api/guides/search-files) guide. *Note:* This method returns *all* files by default, including trashed files. If you don&#39;t want trashed files to appear in the list, use the &#x60;trashed&#x3D;false&#x60; query parameter to remove trashed files from the results.

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
    :param corpora: Bodies of items (files/documents) to which the query applies. Supported bodies are &#39;user&#39;, &#39;domain&#39;, &#39;drive&#39;, and &#39;allDrives&#39;. Prefer &#39;user&#39; or &#39;drive&#39; to &#39;allDrives&#39; for efficiency. By default, corpora is set to &#39;user&#39;. However, this can change depending on the filter set through the &#39;q&#39; parameter.
    :type corpora: str
    :param corpus: Deprecated: The source of files to list. Use &#39;corpora&#39; instead.
    :type corpus: str
    :param drive_id: ID of the shared drive to search.
    :type drive_id: str
    :param include_items_from_all_drives: Whether both My Drive and shared drive items should be included in results.
    :type include_items_from_all_drives: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param include_team_drive_items: Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead.
    :type include_team_drive_items: bool
    :param order_by: A comma-separated list of sort keys. Valid keys are &#39;createdTime&#39;, &#39;folder&#39;, &#39;modifiedByMeTime&#39;, &#39;modifiedTime&#39;, &#39;name&#39;, &#39;name_natural&#39;, &#39;quotaBytesUsed&#39;, &#39;recency&#39;, &#39;sharedWithMeTime&#39;, &#39;starred&#39;, and &#39;viewedByMeTime&#39;. Each key sorts ascending by default, but can be reversed with the &#39;desc&#39; modifier. Example usage: ?orderBy&#x3D;folder,modifiedTime desc,name.
    :type order_by: str
    :param page_size: The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.
    :type page_size: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response.
    :type page_token: str
    :param q: A query for filtering the file results. See the \&quot;Search for files &amp; folders\&quot; guide for supported syntax.
    :type q: str
    :param spaces: A comma-separated list of spaces to query within the corpora. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;.
    :type spaces: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param team_drive_id: Deprecated: Use &#x60;driveId&#x60; instead.
    :type team_drive_id: str

    """
    return web.Response(status=200)


async def drive_files_list_labels(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None) -> web.Response:
    """drive_files_list_labels

    Lists the labels on a file.

    :param file_id: The ID for the file.
    :type file_id: str
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
    :param max_results: The maximum number of labels to return per page. When not set, defaults to 100.
    :type max_results: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)


async def drive_files_modify_labels(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drive_files_modify_labels

    Modifies the set of labels applied to a file. Returns a list of the labels that were added or modified.

    :param file_id: The ID of the file to which the labels belong.
    :type file_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyLabelsRequest.from_dict(body)
    return web.Response(status=200)


async def drive_files_update(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, add_parents=None, enforce_single_parent=None, include_labels=None, include_permissions_for_view=None, keep_revision_forever=None, ocr_language=None, remove_parents=None, supports_all_drives=None, supports_team_drives=None, use_content_as_indexable_text=None, body=None) -> web.Response:
    """drive_files_update

     Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might be changed automatically, such as &#x60;modifiedDate&#x60;. This method supports patch semantics. This method supports an */upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*/*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*/*&#x60; value. The literal &#x60;*/*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads).

    :param file_id: The ID of the file.
    :type file_id: str
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
    :param add_parents: A comma-separated list of parent IDs to add.
    :type add_parents: str
    :param enforce_single_parent: Deprecated: Adding files to multiple folders is no longer supported. Use shortcuts instead.
    :type enforce_single_parent: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param keep_revision_forever: Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
    :type keep_revision_forever: bool
    :param ocr_language: A language hint for OCR processing during image import (ISO 639-1 code).
    :type ocr_language: str
    :param remove_parents: A comma-separated list of parent IDs to remove.
    :type remove_parents: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param use_content_as_indexable_text: Whether to use the uploaded content as indexable text.
    :type use_content_as_indexable_text: bool
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_watch(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, acknowledge_abuse=None, include_labels=None, include_permissions_for_view=None, supports_all_drives=None, supports_team_drives=None, body=None) -> web.Response:
    """drive_files_watch

    Subscribes to changes to a file.

    :param file_id: The ID of the file.
    :type file_id: str
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
    :param acknowledge_abuse: Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt&#x3D;media.
    :type acknowledge_abuse: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
