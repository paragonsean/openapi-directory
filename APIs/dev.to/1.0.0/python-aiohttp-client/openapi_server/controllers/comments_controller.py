from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server import util


async def get_comment_by_id(request: web.Request, id) -> web.Response:
    """Comment by id

    This endpoint allows the client to retrieve a comment as well as his descendants comments.    It will return the required comment (the root) with its nested descendants as a thread.    See the format specification for further details.

    :param id: Comment identifier.
    :type id: int

    """
    return web.Response(status=200)


async def get_comments_by_article_id(request: web.Request, a_id=None, p_id=None) -> web.Response:
    """Comments

    This endpoint allows the client to retrieve all comments belonging to an article or podcast episode as threaded conversations.  It will return the all top level comments with their nested comments as threads. See the format specification for further details.

    :param a_id: Article identifier.
    :type a_id: str
    :param p_id: Podcast Episode identifier.
    :type p_id: str

    """
    return web.Response(status=200)
