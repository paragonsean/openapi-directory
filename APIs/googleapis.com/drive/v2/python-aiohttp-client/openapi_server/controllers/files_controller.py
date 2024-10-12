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


async def drive_files_copy(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, convert=None, enforce_single_parent=None, include_labels=None, include_permissions_for_view=None, ocr=None, ocr_language=None, pinned=None, supports_all_drives=None, supports_team_drives=None, timed_text_language=None, timed_text_track_name=None, visibility=None, body=None) -> web.Response:
    """drive_files_copy

    Creates a copy of the specified file.

    :param file_id: The ID of the file to copy.
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
    :param convert: Whether to convert this file to the corresponding Docs Editors format.
    :type convert: bool
    :param enforce_single_parent: Deprecated: Copying files into multiple folders is no longer supported. Use shortcuts instead.
    :type enforce_single_parent: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param ocr: Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    :type ocr: bool
    :param ocr_language: If &#x60;ocr&#x60; is true, hints at the language to use. Valid values are BCP 47 codes.
    :type ocr_language: str
    :param pinned: Whether to pin the head revision of the new copy. A file can have a maximum of 200 pinned revisions.
    :type pinned: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param timed_text_language: The language of the timed text.
    :type timed_text_language: str
    :param timed_text_track_name: The timed text track name.
    :type timed_text_track_name: str
    :param visibility: The visibility of the new file. This parameter is only relevant when the source is not a native Google Doc and convert&#x3D;false.
    :type visibility: str
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_delete(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, enforce_single_parent=None, supports_all_drives=None, supports_team_drives=None) -> web.Response:
    """drive_files_delete

    Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive, the user must be an &#x60;organizer&#x60; on the parent folder. If the target is a folder, all descendants owned by the user are also deleted.

    :param file_id: The ID of the file to delete.
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
    :param enforce_single_parent: Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner&#39;s root.
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
    :param enforce_single_parent: Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner&#39;s root.
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


async def drive_files_generate_ids(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, space=None, type=None) -> web.Response:
    """drive_files_generate_ids

    Generates a set of file IDs which can be provided in insert or copy requests.

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
    :param max_results: Maximum number of IDs to return.
    :type max_results: int
    :param space: The space in which the IDs can be used to create new files. Supported values are &#x60;drive&#x60; and &#x60;appDataFolder&#x60;. (Default: &#x60;drive&#x60;)
    :type space: str
    :param type: The type of items which the IDs can be used for. Supported values are &#x60;files&#x60; and &#x60;shortcuts&#x60;. Note that &#x60;shortcuts&#x60; are only supported in the &#x60;drive&#x60; &#x60;space&#x60;. (Default: &#x60;files&#x60;)
    :type type: str

    """
    return web.Response(status=200)


async def drive_files_get(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, acknowledge_abuse=None, include_labels=None, include_permissions_for_view=None, projection=None, revision_id=None, supports_all_drives=None, supports_team_drives=None, update_viewed_date=None) -> web.Response:
    """drive_files_get

     Gets a file&#39;s metadata or content by ID. If you provide the URL parameter &#x60;alt&#x3D;media&#x60;, then the response includes the file contents in the response body. Downloading content with &#x60;alt&#x3D;media&#x60; only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [&#x60;files.export&#x60;](/drive/api/reference/rest/v2/files/export) instead. For more information, see [Download &amp; export files](/drive/api/guides/manage-downloads).

    :param file_id: The ID for the file in question.
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
    :param acknowledge_abuse: Whether the user is acknowledging the risk of downloading known malware or other abusive files.
    :type acknowledge_abuse: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param projection: Deprecated: This parameter has no function.
    :type projection: str
    :param revision_id: Specifies the Revision ID that should be downloaded. Ignored unless alt&#x3D;media is specified.
    :type revision_id: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param update_viewed_date: Deprecated: Use &#x60;files.update&#x60; with &#x60;modifiedDateBehavior&#x3D;noChange, updateViewedDate&#x3D;true&#x60; and an empty request body.
    :type update_viewed_date: bool

    """
    return web.Response(status=200)


async def drive_files_insert(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, convert=None, enforce_single_parent=None, include_labels=None, include_permissions_for_view=None, ocr=None, ocr_language=None, pinned=None, supports_all_drives=None, supports_team_drives=None, timed_text_language=None, timed_text_track_name=None, use_content_as_indexable_text=None, visibility=None, body=None) -> web.Response:
    """drive_files_insert

     Inserts a new file. This method supports an */upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*/*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*/*&#x60; value. The literal &#x60;*/*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads). Apps creating shortcuts with &#x60;files.insert&#x60; must specify the MIME type &#x60;application/vnd.google-apps.shortcut&#x60;. Apps should specify a file extension in the &#x60;title&#x60; property when inserting files with the API. For example, an operation to insert a JPEG file should specify something like &#x60;\&quot;title\&quot;: \&quot;cat.jpg\&quot;&#x60; in the metadata. Subsequent &#x60;GET&#x60; requests include the read-only &#x60;fileExtension&#x60; property populated with the extension originally specified in the &#x60;title&#x60; property. When a Google Drive user requests to download a file, or when the file is downloaded through the sync client, Drive builds a full filename (with extension) based on the title. In cases where the extension is missing, Drive attempts to determine the extension based on the file&#39;s MIME type.

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
    :param convert: Whether to convert this file to the corresponding Docs Editors format.
    :type convert: bool
    :param enforce_single_parent: Deprecated: Creating files in multiple folders is no longer supported.
    :type enforce_single_parent: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param ocr: Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    :type ocr: bool
    :param ocr_language: If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
    :type ocr_language: str
    :param pinned: Whether to pin the head revision of the uploaded file. A file can have a maximum of 200 pinned revisions.
    :type pinned: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param timed_text_language: The language of the timed text.
    :type timed_text_language: str
    :param timed_text_track_name: The timed text track name.
    :type timed_text_track_name: str
    :param use_content_as_indexable_text: Whether to use the content as indexable text.
    :type use_content_as_indexable_text: bool
    :param visibility: The visibility of the new file. This parameter is only relevant when convert&#x3D;false.
    :type visibility: str
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, corpora=None, corpus=None, drive_id=None, include_items_from_all_drives=None, include_labels=None, include_permissions_for_view=None, include_team_drive_items=None, max_results=None, order_by=None, page_token=None, projection=None, q=None, spaces=None, supports_all_drives=None, supports_team_drives=None, team_drive_id=None) -> web.Response:
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
    :param corpora: Bodies of items (files/documents) to which the query applies. Supported bodies are &#x60;default&#x60;, &#x60;domain&#x60;, &#x60;drive&#x60; and &#x60;allDrives&#x60;. Prefer &#x60;default&#x60; or &#x60;drive&#x60; to &#x60;allDrives&#x60; for efficiency.
    :type corpora: str
    :param corpus: Deprecated: The body of items (files/documents) to which the query applies. Use &#x60;corpora&#x60; instead.
    :type corpus: str
    :param drive_id: ID of the shared drive to search.
    :type drive_id: str
    :param include_items_from_all_drives: Whether both My Drive and shared drive items should be included in results.
    :type include_items_from_all_drives: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param include_team_drive_items: Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead.
    :type include_team_drive_items: bool
    :param max_results: The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.
    :type max_results: int
    :param order_by: A comma-separated list of sort keys. Valid keys are &#x60;createdDate&#x60;, &#x60;folder&#x60;, &#x60;lastViewedByMeDate&#x60;, &#x60;modifiedByMeDate&#x60;, &#x60;modifiedDate&#x60;, &#x60;quotaBytesUsed&#x60;, &#x60;recency&#x60;, &#x60;sharedWithMeDate&#x60;, &#x60;starred&#x60;, &#x60;title&#x60;, and &#x60;title_natural&#x60;. Each key sorts ascending by default, but may be reversed with the &#x60;desc&#x60; modifier. Example usage: ?orderBy&#x3D;folder,modifiedDate desc,title. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored.
    :type order_by: str
    :param page_token: Page token for files.
    :type page_token: str
    :param projection: Deprecated: This parameter has no function.
    :type projection: str
    :param q: Query string for searching files.
    :type q: str
    :param spaces: A comma-separated list of spaces to query. Supported values are &#x60;drive&#x60;, and &#x60;appDataFolder&#x60;.
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
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from the previous response.
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


async def drive_files_patch(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, add_parents=None, convert=None, enforce_single_parent=None, include_labels=None, include_permissions_for_view=None, modified_date_behavior=None, new_revision=None, ocr=None, ocr_language=None, pinned=None, remove_parents=None, set_modified_date=None, supports_all_drives=None, supports_team_drives=None, timed_text_language=None, timed_text_track_name=None, update_viewed_date=None, use_content_as_indexable_text=None, body=None) -> web.Response:
    """drive_files_patch

    Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics.

    :param file_id: The ID of the file to update.
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
    :param add_parents: Comma-separated list of parent IDs to add.
    :type add_parents: str
    :param convert: Deprecated: This parameter has no function.
    :type convert: bool
    :param enforce_single_parent: Deprecated: Adding files to multiple folders is no longer supported. Use &#x60;shortcuts&#x60; instead.
    :type enforce_single_parent: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param modified_date_behavior: Determines the behavior in which &#x60;modifiedDate&#x60; is updated. This overrides &#x60;setModifiedDate&#x60;.
    :type modified_date_behavior: str
    :param new_revision: Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). Note that this field is ignored if there is no payload in the request.
    :type new_revision: bool
    :param ocr: Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    :type ocr: bool
    :param ocr_language: If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
    :type ocr_language: str
    :param pinned: Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. Note that this field is ignored if there is no payload in the request.
    :type pinned: bool
    :param remove_parents: Comma-separated list of parent IDs to remove.
    :type remove_parents: str
    :param set_modified_date: Whether to set the modified date using the value supplied in the request body. Setting this field to &#x60;true&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;fromBodyOrNow&#x60;, and &#x60;false&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;now&#x60;. To prevent any changes to the modified date set &#x60;modifiedDateBehavior&#x3D;noChange&#x60;.
    :type set_modified_date: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param timed_text_language: The language of the timed text.
    :type timed_text_language: str
    :param timed_text_track_name: The timed text track name.
    :type timed_text_track_name: str
    :param update_viewed_date: Whether to update the view date after successfully updating the file.
    :type update_viewed_date: bool
    :param use_content_as_indexable_text: Whether to use the content as indexable text.
    :type use_content_as_indexable_text: bool
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_touch(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_labels=None, include_permissions_for_view=None, supports_all_drives=None, supports_team_drives=None) -> web.Response:
    """drive_files_touch

    Set the file&#39;s updated time to the current server time.

    :param file_id: The ID of the file to update.
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
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool

    """
    return web.Response(status=200)


async def drive_files_trash(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_labels=None, include_permissions_for_view=None, supports_all_drives=None, supports_team_drives=None) -> web.Response:
    """drive_files_trash

    Moves a file to the trash. The currently authenticated user must own the file or be at least a &#x60;fileOrganizer&#x60; on the parent for shared drive files.

    :param file_id: The ID of the file to trash.
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
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool

    """
    return web.Response(status=200)


async def drive_files_untrash(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_labels=None, include_permissions_for_view=None, supports_all_drives=None, supports_team_drives=None) -> web.Response:
    """drive_files_untrash

    Restores a file from the trash. The currently authenticated user must own the file or be at least a &#x60;fileOrganizer&#x60; on the parent for shared drive files.

    :param file_id: The ID of the file to untrash.
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
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool

    """
    return web.Response(status=200)


async def drive_files_update(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, add_parents=None, convert=None, enforce_single_parent=None, include_labels=None, include_permissions_for_view=None, modified_date_behavior=None, new_revision=None, ocr=None, ocr_language=None, pinned=None, remove_parents=None, set_modified_date=None, supports_all_drives=None, supports_team_drives=None, timed_text_language=None, timed_text_track_name=None, update_viewed_date=None, use_content_as_indexable_text=None, body=None) -> web.Response:
    """drive_files_update

     Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might be changed automatically, such as &#x60;modifiedDate&#x60;. This method supports patch semantics. This method supports an */upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*/*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*/*&#x60; value. The literal &#x60;*/*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads).

    :param file_id: The ID of the file to update.
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
    :param add_parents: Comma-separated list of parent IDs to add.
    :type add_parents: str
    :param convert: Deprecated: This parameter has no function.
    :type convert: bool
    :param enforce_single_parent: Deprecated: Adding files to multiple folders is no longer supported. Use &#x60;shortcuts&#x60; instead.
    :type enforce_single_parent: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param modified_date_behavior: Determines the behavior in which &#x60;modifiedDate&#x60; is updated. This overrides &#x60;setModifiedDate&#x60;.
    :type modified_date_behavior: str
    :param new_revision: Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045).
    :type new_revision: bool
    :param ocr: Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
    :type ocr: bool
    :param ocr_language: If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
    :type ocr_language: str
    :param pinned: Whether to pin the new revision. A file can have a maximum of 200 pinned revisions.
    :type pinned: bool
    :param remove_parents: Comma-separated list of parent IDs to remove.
    :type remove_parents: str
    :param set_modified_date: Whether to set the modified date using the value supplied in the request body. Setting this field to &#x60;true&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;fromBodyOrNow&#x60;, and &#x60;false&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;now&#x60;. To prevent any changes to the modified date set &#x60;modifiedDateBehavior&#x3D;noChange&#x60;.
    :type set_modified_date: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param timed_text_language: The language of the timed text.
    :type timed_text_language: str
    :param timed_text_track_name: The timed text track name.
    :type timed_text_track_name: str
    :param update_viewed_date: Whether to update the view date after successfully updating the file.
    :type update_viewed_date: bool
    :param use_content_as_indexable_text: Whether to use the content as indexable text.
    :type use_content_as_indexable_text: bool
    :param body: 
    :type body: dict | bytes

    """
    body = File.from_dict(body)
    return web.Response(status=200)


async def drive_files_watch(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, acknowledge_abuse=None, include_labels=None, include_permissions_for_view=None, projection=None, revision_id=None, supports_all_drives=None, supports_team_drives=None, update_viewed_date=None, body=None) -> web.Response:
    """drive_files_watch

    Subscribes to changes to a file.

    :param file_id: The ID for the file in question.
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
    :param acknowledge_abuse: Whether the user is acknowledging the risk of downloading known malware or other abusive files.
    :type acknowledge_abuse: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param projection: Deprecated: This parameter has no function.
    :type projection: str
    :param revision_id: Specifies the Revision ID that should be downloaded. Ignored unless alt&#x3D;media is specified.
    :type revision_id: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param update_viewed_date: Deprecated: Use files.update with modifiedDateBehavior&#x3D;noChange, updateViewedDate&#x3D;true and an empty request body.
    :type update_viewed_date: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
