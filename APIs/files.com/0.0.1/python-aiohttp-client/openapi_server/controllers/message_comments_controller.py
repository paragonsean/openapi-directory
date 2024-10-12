from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_comment_entity import MessageCommentEntity
from openapi_server import util


async def delete_message_comments_id(request: web.Request, id) -> web.Response:
    """Delete Message Comment

    Delete Message Comment

    :param id: Message Comment ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_message_comments(request: web.Request, message_id, user_id=None, cursor=None, per_page=None) -> web.Response:
    """List Message Comments

    List Message Comments

    :param message_id: Message comment to return comments for.
    :type message_id: int
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_message_comments_id(request: web.Request, id) -> web.Response:
    """Show Message Comment

    Show Message Comment

    :param id: Message Comment ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_message_comments_id(request: web.Request, id, body) -> web.Response:
    """Update Message Comment

    Update Message Comment

    :param id: Message Comment ID.
    :type id: int
    :param body: Comment body.
    :type body: str

    """
    return web.Response(status=200)


async def post_message_comments(request: web.Request, body, user_id=None) -> web.Response:
    """Create Message Comment

    Create Message Comment

    :param body: Comment body.
    :type body: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    return web.Response(status=200)
