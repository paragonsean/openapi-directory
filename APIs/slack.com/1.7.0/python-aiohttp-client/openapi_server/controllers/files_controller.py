from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server.models.files_comments_delete_error_schema import FilesCommentsDeleteErrorSchema
from openapi_server.models.files_comments_delete_schema import FilesCommentsDeleteSchema
from openapi_server.models.files_delete_error_schema import FilesDeleteErrorSchema
from openapi_server.models.files_delete_schema import FilesDeleteSchema
from openapi_server.models.files_info_error_schema import FilesInfoErrorSchema
from openapi_server.models.files_info_schema import FilesInfoSchema
from openapi_server.models.files_list_error_schema import FilesListErrorSchema
from openapi_server.models.files_list_schema import FilesListSchema
from openapi_server.models.files_revoke_public_url_error_schema import FilesRevokePublicURLErrorSchema
from openapi_server.models.files_revoke_public_url_schema import FilesRevokePublicURLSchema
from openapi_server.models.files_shared_public_url_error_schema import FilesSharedPublicURLErrorSchema
from openapi_server.models.files_shared_public_url_schema import FilesSharedPublicURLSchema
from openapi_server.models.files_upload_error_schema import FilesUploadErrorSchema
from openapi_server.models.files_upload_schema import FilesUploadSchema
from openapi_server import util


async def files_comments_delete_0(request: web.Request, token=None, file=None, id=None) -> web.Response:
    """files_comments_delete_0

    Deletes an existing comment on a file.

    :param token: Authentication token. Requires scope: &#x60;files:write:user&#x60;
    :type token: str
    :param file: File to delete a comment from.
    :type file: str
    :param id: The comment to delete.
    :type id: str

    """
    return web.Response(status=200)


async def files_delete(request: web.Request, token=None, file=None) -> web.Response:
    """files_delete

    Deletes a file.

    :param token: Authentication token. Requires scope: &#x60;files:write:user&#x60;
    :type token: str
    :param file: ID of file to delete.
    :type file: str

    """
    return web.Response(status=200)


async def files_info(request: web.Request, token=None, file=None, count=None, page=None, limit=None, cursor=None) -> web.Response:
    """files_info

    Gets information about a file.

    :param token: Authentication token. Requires scope: &#x60;files:read&#x60;
    :type token: str
    :param file: Specify a file by providing its ID.
    :type file: str
    :param count: 
    :type count: str
    :param page: 
    :type page: str
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached.
    :type limit: int
    :param cursor: Parameter for pagination. File comments are paginated for a single file. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection of comments. See [pagination](/docs/pagination) for more details.
    :type cursor: str

    """
    return web.Response(status=200)


async def files_list(request: web.Request, token=None, user=None, channel=None, ts_from=None, ts_to=None, types=None, count=None, page=None, show_files_hidden_by_limit=None) -> web.Response:
    """files_list

    List for a team, in a channel, or from a user with applied filters.

    :param token: Authentication token. Requires scope: &#x60;files:read&#x60;
    :type token: str
    :param user: Filter files created by a single user.
    :type user: str
    :param channel: Filter files appearing in a specific channel, indicated by its ID.
    :type channel: str
    :param ts_from: Filter files created after this timestamp (inclusive).
    :type ts_from: 
    :param ts_to: Filter files created before this timestamp (inclusive).
    :type ts_to: 
    :param types: Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like &#x60;types&#x3D;spaces,snippets&#x60;.The default value is &#x60;all&#x60;, which does not filter the list.
    :type types: str
    :param count: 
    :type count: str
    :param page: 
    :type page: str
    :param show_files_hidden_by_limit: Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.
    :type show_files_hidden_by_limit: bool

    """
    return web.Response(status=200)


async def files_remote_add_0(request: web.Request, external_id=None, external_url=None, filetype=None, indexable_file_contents=None, preview_image=None, title=None, token=None) -> web.Response:
    """files_remote_add_0

    Adds a file from a remote service

    :param external_id: Creator defined GUID for the file.
    :type external_id: str
    :param external_url: URL of the remote file.
    :type external_url: str
    :param filetype: type of file
    :type filetype: str
    :param indexable_file_contents: A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
    :type indexable_file_contents: str
    :param preview_image: Preview of the document via &#x60;multipart/form-data&#x60;.
    :type preview_image: str
    :param title: Title of the file being shared.
    :type title: str
    :param token: Authentication token. Requires scope: &#x60;remote_files:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def files_remote_info_0(request: web.Request, token=None, file=None, external_id=None) -> web.Response:
    """files_remote_info_0

    Retrieve information about a remote file added to Slack

    :param token: Authentication token. Requires scope: &#x60;remote_files:read&#x60;
    :type token: str
    :param file: Specify a file by providing its ID.
    :type file: str
    :param external_id: Creator defined GUID for the file.
    :type external_id: str

    """
    return web.Response(status=200)


async def files_remote_list_0(request: web.Request, token=None, channel=None, ts_from=None, ts_to=None, limit=None, cursor=None) -> web.Response:
    """files_remote_list_0

    Retrieve information about a remote file added to Slack

    :param token: Authentication token. Requires scope: &#x60;remote_files:read&#x60;
    :type token: str
    :param channel: Filter files appearing in a specific channel, indicated by its ID.
    :type channel: str
    :param ts_from: Filter files created after this timestamp (inclusive).
    :type ts_from: 
    :param ts_to: Filter files created before this timestamp (inclusive).
    :type ts_to: 
    :param limit: The maximum number of items to return.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str

    """
    return web.Response(status=200)


async def files_remote_remove_0(request: web.Request, external_id=None, file=None, token=None) -> web.Response:
    """files_remote_remove_0

    Remove a remote file.

    :param external_id: Creator defined GUID for the file.
    :type external_id: str
    :param file: Specify a file by providing its ID.
    :type file: str
    :param token: Authentication token. Requires scope: &#x60;remote_files:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def files_remote_share_0(request: web.Request, token=None, file=None, external_id=None, channels=None) -> web.Response:
    """files_remote_share_0

    Share a remote file into a channel.

    :param token: Authentication token. Requires scope: &#x60;remote_files:share&#x60;
    :type token: str
    :param file: Specify a file registered with Slack by providing its ID. Either this field or &#x60;external_id&#x60; or both are required.
    :type file: str
    :param external_id: The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or &#x60;file&#x60; or both are required.
    :type external_id: str
    :param channels: Comma-separated list of channel IDs where the file will be shared.
    :type channels: str

    """
    return web.Response(status=200)


async def files_remote_update_0(request: web.Request, external_id=None, external_url=None, file=None, filetype=None, indexable_file_contents=None, preview_image=None, title=None, token=None) -> web.Response:
    """files_remote_update_0

    Updates an existing remote file.

    :param external_id: Creator defined GUID for the file.
    :type external_id: str
    :param external_url: URL of the remote file.
    :type external_url: str
    :param file: Specify a file by providing its ID.
    :type file: str
    :param filetype: type of file
    :type filetype: str
    :param indexable_file_contents: File containing contents that can be used to improve searchability for the remote file.
    :type indexable_file_contents: str
    :param preview_image: Preview of the document via &#x60;multipart/form-data&#x60;.
    :type preview_image: str
    :param title: Title of the file being shared.
    :type title: str
    :param token: Authentication token. Requires scope: &#x60;remote_files:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def files_revoke_public_url(request: web.Request, token=None, file=None) -> web.Response:
    """files_revoke_public_url

    Revokes public/external sharing access for a file

    :param token: Authentication token. Requires scope: &#x60;files:write:user&#x60;
    :type token: str
    :param file: File to revoke
    :type file: str

    """
    return web.Response(status=200)


async def files_shared_public_url(request: web.Request, token=None, file=None) -> web.Response:
    """files_shared_public_url

    Enables a file for public/external sharing.

    :param token: Authentication token. Requires scope: &#x60;files:write:user&#x60;
    :type token: str
    :param file: File to share
    :type file: str

    """
    return web.Response(status=200)


async def files_upload(request: web.Request, channels=None, content=None, file=None, filename=None, filetype=None, initial_comment=None, thread_ts=None, title=None, token=None) -> web.Response:
    """files_upload

    Uploads or creates a file.

    :param channels: Comma-separated list of channel names or IDs where the file will be shared.
    :type channels: str
    :param content: File contents via a POST variable. If omitting this parameter, you must provide a &#x60;file&#x60;.
    :type content: str
    :param file: File contents via &#x60;multipart/form-data&#x60;. If omitting this parameter, you must submit &#x60;content&#x60;.
    :type file: str
    :param filename: Filename of file.
    :type filename: str
    :param filetype: A [file type](/types/file#file_types) identifier.
    :type filetype: str
    :param initial_comment: The message text introducing the file in specified &#x60;channels&#x60;.
    :type initial_comment: str
    :param thread_ts: Provide another message&#39;s &#x60;ts&#x60; value to upload this file as a reply. Never use a reply&#39;s &#x60;ts&#x60; value; use its parent instead.
    :type thread_ts: 
    :param title: Title of file.
    :type title: str
    :param token: Authentication token. Requires scope: &#x60;files:write:user&#x60;
    :type token: str

    """
    return web.Response(status=200)
