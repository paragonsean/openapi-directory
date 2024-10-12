from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.comment_editable import CommentEditable
from openapi_server import util


async def comments_id_delete(request: web.Request, id) -> web.Response:
    """Delete comment

    Delete comment.

    :param id: Comment id
    :type id: int

    """
    return web.Response(status=200)


async def comments_id_patch(request: web.Request, id, comment=None) -> web.Response:
    """Update comment

    Update comment. Wrap comment parameters in [comment].

    :param id: Comment id
    :type id: int
    :param comment: Comment attributes
    :type comment: dict | bytes

    """
    comment = CommentEditable.from_dict(comment)
    return web.Response(status=200)


async def maps_id_comments_get(request: web.Request, id) -> web.Response:
    """List comments for a given map

    List comments for a given map.

    :param id: Id of map
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_comments_post(request: web.Request, id, comment=None) -> web.Response:
    """Create map comment

    Create map comment. Wrap comment parameters in [comment].

    :param id: map id
    :type id: int
    :param comment: comment attributes
    :type comment: dict | bytes

    """
    comment = CommentEditable.from_dict(comment)
    return web.Response(status=200)


async def spots_id_comments_get(request: web.Request, id) -> web.Response:
    """List comments for a given spot

    List comments for a given spot.

    :param id: Id of spot
    :type id: int

    """
    return web.Response(status=200)


async def spots_id_comments_post(request: web.Request, id, comment=None) -> web.Response:
    """Create spot comment

    Create spot comment. Wrap comment parameters in [comment].

    :param id: spot id
    :type id: int
    :param comment: comment attributes
    :type comment: dict | bytes

    """
    comment = CommentEditable.from_dict(comment)
    return web.Response(status=200)
