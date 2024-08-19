from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def all_players_search(request: web.Request, search=None) -> web.Response:
    """all players (search)

    all players (search)

    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def specific_player(request: web.Request, ) -> web.Response:
    """specific player

    specific player


    """
    return web.Response(status=200)
