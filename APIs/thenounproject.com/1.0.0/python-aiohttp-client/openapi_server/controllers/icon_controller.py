from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_icon_by_id(request: web.Request, id) -> web.Response:
    """Get icon by id

    Returns a single icon

    :param id: Icon id
    :type id: int

    """
    return web.Response(status=200)


async def get_icon_by_term(request: web.Request, term) -> web.Response:
    """Get icon by term

    Returns a single icon

    :param term: Icon term
    :type term: str

    """
    return web.Response(status=200)
