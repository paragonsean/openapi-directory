from typing import List, Dict
from aiohttp import web

from openapi_server.models.lock_entity import LockEntity
from openapi_server import util


async def delete_locks_path(request: web.Request, path, token) -> web.Response:
    """Delete Lock

    Delete Lock

    :param path: Path
    :type path: str
    :param token: Lock token
    :type token: str

    """
    return web.Response(status=200)


async def lock_list_for_path(request: web.Request, path, cursor=None, per_page=None, include_children=None) -> web.Response:
    """List Locks by path

    List Locks by path

    :param path: Path to operate on.
    :type path: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param include_children: Include locks from children objects?
    :type include_children: bool

    """
    return web.Response(status=200)


async def post_locks_path(request: web.Request, path, allow_access_by_any_user=None, exclusive=None, recursive=None, timeout=None) -> web.Response:
    """Create Lock

    Create Lock

    :param path: Path
    :type path: str
    :param allow_access_by_any_user: Allow lock to be updated by any user?
    :type allow_access_by_any_user: bool
    :param exclusive: Is lock exclusive?
    :type exclusive: bool
    :param recursive: Does lock apply to subfolders?
    :type recursive: str
    :param timeout: Lock timeout length
    :type timeout: int

    """
    return web.Response(status=200)
