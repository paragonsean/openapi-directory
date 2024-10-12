from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.piece import Piece
from openapi_server import util


async def api_v2_pieces_get(request: web.Request, episode_id) -> web.Response:
    """Returns the pieces matching the query parameters.

    

    :param episode_id: The ID of the episode that owns the piece.
    :type episode_id: int

    """
    return web.Response(status=200)


async def api_v2_pieces_id_delete(request: web.Request, id) -> web.Response:
    """Deletes the piece with the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_pieces_id_get(request: web.Request, id) -> web.Response:
    """Returns the piece matching the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_pieces_post(request: web.Request, body=None) -> web.Response:
    """Create a new piece.

    

    :param body: 
    :type body: dict | bytes

    """
    body = Piece.from_dict(body)
    return web.Response(status=200)
