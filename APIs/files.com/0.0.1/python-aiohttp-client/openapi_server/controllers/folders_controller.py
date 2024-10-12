from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_entity import FileEntity
from openapi_server import util


async def folder_list_for_path(request: web.Request, path, cursor=None, per_page=None, filter=None, preview_size=None, sort_by=None, search=None, search_all=None, with_previews=None, with_priority_color=None) -> web.Response:
    """List Folders by path

    List Folders by path

    :param path: Path to operate on.
    :type path: str
    :param cursor: Send cursor to resume an existing list from the point at which you left off.  Get a cursor from an existing list via the X-Files-Cursor-Next header or the X-Files-Cursor-Prev header.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param filter: If specified, will filter folders/files list by this string.  Wildcards of &#x60;*&#x60; and &#x60;?&#x60; are acceptable here.
    :type filter: str
    :param preview_size: Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;.
    :type preview_size: str
    :param sort_by: Search by field and direction. Valid fields are &#x60;path&#x60;, &#x60;size&#x60;, &#x60;modified_at_datetime&#x60;, &#x60;provided_modified_at&#x60;.  Valid directions are &#x60;asc&#x60; and &#x60;desc&#x60;.  Defaults to &#x60;{\&quot;path\&quot;:\&quot;asc\&quot;}&#x60;.
    :type sort_by: dict | bytes
    :param search: If &#x60;search_all&#x60; is &#x60;true&#x60;, provide the search string here.  Otherwise, this parameter acts like an alias of &#x60;filter&#x60;.
    :type search: str
    :param search_all: Search entire site?  If set, we will ignore the folder path provided and search the entire site.  This is the same API used by the search bar in the UI.  Search results are a best effort, not real time, and not guaranteed to match every file.  This field should only be used for ad-hoc (human) searching, and not as part of an automated process.
    :type search_all: bool
    :param with_previews: Include file previews?
    :type with_previews: bool
    :param with_priority_color: Include file priority color information?
    :type with_priority_color: bool

    """
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def post_folders_path(request: web.Request, path, mkdir_parents=None, provided_mtime=None) -> web.Response:
    """Create folder

    Create folder

    :param path: Path to operate on.
    :type path: str
    :param mkdir_parents: Create parent directories if they do not exist?
    :type mkdir_parents: bool
    :param provided_mtime: User provided modification time.
    :type provided_mtime: str

    """
    provided_mtime = util.deserialize_datetime(provided_mtime)
    return web.Response(status=200)
