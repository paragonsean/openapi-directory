from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_action_entity import FileActionEntity
from openapi_server.models.file_entity import FileEntity
from openapi_server.models.file_upload_part_entity import FileUploadPartEntity
from openapi_server import util


async def file_action_begin_upload(request: web.Request, path, mkdir_parents=None, part=None, parts=None, ref=None, restart=None, size=None, with_rename=None) -> web.Response:
    """Begin file upload

    Begin file upload

    :param path: Path to operate on.
    :type path: str
    :param mkdir_parents: Create parent directories if they do not exist?
    :type mkdir_parents: bool
    :param part: Part if uploading a part.
    :type part: int
    :param parts: How many parts to fetch?
    :type parts: int
    :param ref: 
    :type ref: str
    :param restart: File byte offset to restart from.
    :type restart: int
    :param size: Total bytes of file being uploaded (include bytes being retained if appending/restarting).
    :type size: int
    :param with_rename: Allow file rename instead of overwrite?
    :type with_rename: bool

    """
    return web.Response(status=200)


async def file_action_copy(request: web.Request, path, destination, structure=None) -> web.Response:
    """Copy file/folder

    Copy file/folder

    :param path: Path to operate on.
    :type path: str
    :param destination: Copy destination path.
    :type destination: str
    :param structure: Copy structure only?
    :type structure: bool

    """
    return web.Response(status=200)


async def file_action_find(request: web.Request, path, preview_size=None, with_previews=None, with_priority_color=None) -> web.Response:
    """Find file/folder by path

    Find file/folder by path

    :param path: Path to operate on.
    :type path: str
    :param preview_size: Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;.
    :type preview_size: str
    :param with_previews: Include file preview information?
    :type with_previews: bool
    :param with_priority_color: Include file priority color information?
    :type with_priority_color: bool

    """
    return web.Response(status=200)


async def file_action_move(request: web.Request, path, destination) -> web.Response:
    """Move file/folder

    Move file/folder

    :param path: Path to operate on.
    :type path: str
    :param destination: Move destination path.
    :type destination: str

    """
    return web.Response(status=200)
