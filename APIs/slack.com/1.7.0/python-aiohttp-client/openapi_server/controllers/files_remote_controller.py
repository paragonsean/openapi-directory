from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def files_remote_add(request: web.Request, external_id=None, external_url=None, filetype=None, indexable_file_contents=None, preview_image=None, title=None, token=None) -> web.Response:
    """files_remote_add

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


async def files_remote_info(request: web.Request, token=None, file=None, external_id=None) -> web.Response:
    """files_remote_info

    Retrieve information about a remote file added to Slack

    :param token: Authentication token. Requires scope: &#x60;remote_files:read&#x60;
    :type token: str
    :param file: Specify a file by providing its ID.
    :type file: str
    :param external_id: Creator defined GUID for the file.
    :type external_id: str

    """
    return web.Response(status=200)


async def files_remote_list(request: web.Request, token=None, channel=None, ts_from=None, ts_to=None, limit=None, cursor=None) -> web.Response:
    """files_remote_list

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


async def files_remote_remove(request: web.Request, external_id=None, file=None, token=None) -> web.Response:
    """files_remote_remove

    Remove a remote file.

    :param external_id: Creator defined GUID for the file.
    :type external_id: str
    :param file: Specify a file by providing its ID.
    :type file: str
    :param token: Authentication token. Requires scope: &#x60;remote_files:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def files_remote_share(request: web.Request, token=None, file=None, external_id=None, channels=None) -> web.Response:
    """files_remote_share

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


async def files_remote_update(request: web.Request, external_id=None, external_url=None, file=None, filetype=None, indexable_file_contents=None, preview_image=None, title=None, token=None) -> web.Response:
    """files_remote_update

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
