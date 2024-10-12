from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_entity import MessageEntity
from openapi_server import util


async def delete_messages_id(request: web.Request, id) -> web.Response:
    """Delete Message

    Delete Message

    :param id: Message ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_messages(request: web.Request, project_id, user_id=None, cursor=None, per_page=None) -> web.Response:
    """List Messages

    List Messages

    :param project_id: Project for which to return messages.
    :type project_id: int
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_messages_id(request: web.Request, id) -> web.Response:
    """Show Message

    Show Message

    :param id: Message ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_messages_id(request: web.Request, id, body, project_id, subject) -> web.Response:
    """Update Message

    Update Message

    :param id: Message ID.
    :type id: int
    :param body: Message body.
    :type body: str
    :param project_id: Project to which the message should be attached.
    :type project_id: int
    :param subject: Message subject.
    :type subject: str

    """
    return web.Response(status=200)


async def post_messages(request: web.Request, body, project_id, subject, user_id=None) -> web.Response:
    """Create Message

    Create Message

    :param body: Message body.
    :type body: str
    :param project_id: Project to which the message should be attached.
    :type project_id: int
    :param subject: Message subject.
    :type subject: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    return web.Response(status=200)
