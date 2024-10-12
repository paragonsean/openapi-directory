from typing import List, Dict
from aiohttp import web

from openapi_server.models.files_comments_delete_error_schema import FilesCommentsDeleteErrorSchema
from openapi_server.models.files_comments_delete_schema import FilesCommentsDeleteSchema
from openapi_server import util


async def files_comments_delete(request: web.Request, token=None, file=None, id=None) -> web.Response:
    """files_comments_delete

    Deletes an existing comment on a file.

    :param token: Authentication token. Requires scope: &#x60;files:write:user&#x60;
    :type token: str
    :param file: File to delete a comment from.
    :type file: str
    :param id: The comment to delete.
    :type id: str

    """
    return web.Response(status=200)
