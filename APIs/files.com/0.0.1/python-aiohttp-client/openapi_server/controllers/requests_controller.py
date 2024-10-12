from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_entity import RequestEntity
from openapi_server import util


async def delete_requests_id(request: web.Request, id) -> web.Response:
    """Delete Request

    Delete Request

    :param id: Request ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_requests(request: web.Request, cursor=None, per_page=None, sort_by=None, mine=None, path=None) -> web.Response:
    """List Requests

    List Requests

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[destination]&#x3D;desc&#x60;). Valid fields are &#x60;destination&#x60;.
    :type sort_by: dict | bytes
    :param mine: Only show requests of the current user?  (Defaults to true if current user is not a site admin.)
    :type mine: bool
    :param path: Path to show requests for.  If omitted, shows all paths. Send &#x60;/&#x60; to represent the root directory.
    :type path: str

    """
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def get_requests_folders_path(request: web.Request, path, cursor=None, per_page=None, sort_by=None, mine=None) -> web.Response:
    """List Requests

    List Requests

    :param path: Path to show requests for.  If omitted, shows all paths. Send &#x60;/&#x60; to represent the root directory.
    :type path: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[destination]&#x3D;desc&#x60;). Valid fields are &#x60;destination&#x60;.
    :type sort_by: dict | bytes
    :param mine: Only show requests of the current user?  (Defaults to true if current user is not a site admin.)
    :type mine: bool

    """
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def post_requests(request: web.Request, destination, path, group_ids=None, user_ids=None) -> web.Response:
    """Create Request

    Create Request

    :param destination: Destination filename (without extension) to request.
    :type destination: str
    :param path: Folder path on which to request the file.
    :type path: str
    :param group_ids: A list of group IDs to request the file from. If sent as a string, it should be comma-delimited.
    :type group_ids: str
    :param user_ids: A list of user IDs to request the file from. If sent as a string, it should be comma-delimited.
    :type user_ids: str

    """
    return web.Response(status=200)
