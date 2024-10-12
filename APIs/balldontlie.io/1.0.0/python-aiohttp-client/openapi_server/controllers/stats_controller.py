from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def all_stats_example_parameters(request: web.Request, season=None, player_ids=None) -> web.Response:
    """all stats (example parameters)

    all stats (example parameters)

    :param season: 
    :type season: str
    :param player_ids: 
    :type player_ids: str

    """
    return web.Response(status=200)
