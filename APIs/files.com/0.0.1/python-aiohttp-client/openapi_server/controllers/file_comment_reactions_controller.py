from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_comment_reaction_entity import FileCommentReactionEntity
from openapi_server import util


async def delete_file_comment_reactions_id(request: web.Request, id) -> web.Response:
    """Delete File Comment Reaction

    Delete File Comment Reaction

    :param id: File Comment Reaction ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_file_comment_reactions(request: web.Request, emoji, file_comment_id, user_id=None) -> web.Response:
    """Create File Comment Reaction

    Create File Comment Reaction

    :param emoji: Emoji to react with.
    :type emoji: str
    :param file_comment_id: ID of file comment to attach reaction to.
    :type file_comment_id: int
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    return web.Response(status=200)
