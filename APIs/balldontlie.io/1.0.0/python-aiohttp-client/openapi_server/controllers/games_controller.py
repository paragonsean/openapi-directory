from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def all_games_example_parameters(request: web.Request, seasons=None, team_ids=None) -> web.Response:
    """all games (example parameters)

    all games (example parameters)

    :param seasons: 
    :type seasons: str
    :param team_ids: 
    :type team_ids: str

    """
    return web.Response(status=200)


async def specific_game(request: web.Request, ) -> web.Response:
    """specific game

    specific game


    """
    return web.Response(status=200)
