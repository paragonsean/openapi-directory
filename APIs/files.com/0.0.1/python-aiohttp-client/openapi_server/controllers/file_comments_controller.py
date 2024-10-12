from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_comment_entity import FileCommentEntity
from openapi_server import util


async def delete_file_comments_id(request: web.Request, id) -> web.Response:
    """Delete File Comment

    Delete File Comment

    :param id: File Comment ID.
    :type id: int

    """
    return web.Response(status=200)


async def file_comment_list_for_path(request: web.Request, path, cursor=None, per_page=None) -> web.Response:
    """List File Comments by path

    List File Comments by path

    :param path: Path to operate on.
    :type path: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def patch_file_comments_id(request: web.Request, id, body) -> web.Response:
    """Update File Comment

    Update File Comment

    :param id: File Comment ID.
    :type id: int
    :param body: Comment body.
    :type body: str

    """
    return web.Response(status=200)


async def post_file_comments(request: web.Request, body, path) -> web.Response:
    """Create File Comment

    Create File Comment

    :param body: Comment body.
    :type body: str
    :param path: File path.
    :type path: str

    """
    return web.Response(status=200)
