from typing import List, Dict
from aiohttp import web

from openapi_server.models.priority_entity import PriorityEntity
from openapi_server import util


async def get_priorities(request: web.Request, path, cursor=None, per_page=None) -> web.Response:
    """List Priorities

    List Priorities

    :param path: The path to query for priorities
    :type path: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)
