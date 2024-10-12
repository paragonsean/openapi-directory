from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_reaction_entity import MessageReactionEntity
from openapi_server import util


async def delete_message_reactions_id(request: web.Request, id) -> web.Response:
    """Delete Message Reaction

    Delete Message Reaction

    :param id: Message Reaction ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_message_reactions(request: web.Request, message_id, user_id=None, cursor=None, per_page=None) -> web.Response:
    """List Message Reactions

    List Message Reactions

    :param message_id: Message to return reactions for.
    :type message_id: int
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_message_reactions_id(request: web.Request, id) -> web.Response:
    """Show Message Reaction

    Show Message Reaction

    :param id: Message Reaction ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_message_reactions(request: web.Request, emoji, user_id=None) -> web.Response:
    """Create Message Reaction

    Create Message Reaction

    :param emoji: Emoji to react with.
    :type emoji: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    return web.Response(status=200)
