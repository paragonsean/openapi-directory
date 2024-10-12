from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_entity import FileEntity
from openapi_server import util


async def delete_files_path(request: web.Request, path, recursive=None) -> web.Response:
    """Delete file/folder

    Delete file/folder

    :param path: Path to operate on.
    :type path: str
    :param recursive: If true, will recursively delete folers.  Otherwise, will error on non-empty folders.
    :type recursive: bool

    """
    return web.Response(status=200)


async def file_download(request: web.Request, path, action=None, preview_size=None, with_previews=None, with_priority_color=None) -> web.Response:
    """Download file

    Download file

    :param path: Path to operate on.
    :type path: str
    :param action: Can be blank, &#x60;redirect&#x60; or &#x60;stat&#x60;.  If set to &#x60;stat&#x60;, we will return file information but without a download URL, and without logging a download.  If set to &#x60;redirect&#x60; we will serve a 302 redirect directly to the file.  This is used for integrations with Zapier, and is not recommended for most integrations.
    :type action: str
    :param preview_size: Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;.
    :type preview_size: str
    :param with_previews: Include file preview information?
    :type with_previews: bool
    :param with_priority_color: Include file priority color information?
    :type with_priority_color: bool

    """
    return web.Response(status=200)


async def patch_files_path(request: web.Request, path, priority_color=None, provided_mtime=None) -> web.Response:
    """Update file/folder metadata

    Update file/folder metadata

    :param path: Path to operate on.
    :type path: str
    :param priority_color: Priority/Bookmark color of file.
    :type priority_color: str
    :param provided_mtime: Modified time of file.
    :type provided_mtime: str

    """
    provided_mtime = util.deserialize_datetime(provided_mtime)
    return web.Response(status=200)


async def post_files_path(request: web.Request, path, etags_etag, etags_part, action=None, length=None, mkdir_parents=None, part=None, parts=None, provided_mtime=None, ref=None, restart=None, size=None, structure=None, with_rename=None) -> web.Response:
    """Upload file

    Upload file

    :param path: Path to operate on.
    :type path: str
    :param etags_etag: etag identifier.
    :type etags_etag: List[str]
    :param etags_part: Part number.
    :type etags_part: List[int]
    :param action: The action to perform.  Can be &#x60;append&#x60;, &#x60;attachment&#x60;, &#x60;end&#x60;, &#x60;upload&#x60;, &#x60;put&#x60;, or may not exist
    :type action: str
    :param length: Length of file.
    :type length: int
    :param mkdir_parents: Create parent directories if they do not exist?
    :type mkdir_parents: bool
    :param part: Part if uploading a part.
    :type part: int
    :param parts: How many parts to fetch?
    :type parts: int
    :param provided_mtime: User provided modification time.
    :type provided_mtime: str
    :param ref: 
    :type ref: str
    :param restart: File byte offset to restart from.
    :type restart: int
    :param size: Size of file.
    :type size: int
    :param structure: If copying folder, copy just the structure?
    :type structure: str
    :param with_rename: Allow file rename instead of overwrite?
    :type with_rename: bool

    """
    provided_mtime = util.deserialize_datetime(provided_mtime)
    return web.Response(status=200)
