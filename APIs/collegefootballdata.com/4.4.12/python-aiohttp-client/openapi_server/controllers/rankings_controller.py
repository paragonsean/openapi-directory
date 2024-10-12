from typing import List, Dict
from aiohttp import web

from openapi_server.models.ranking_week import RankingWeek
from openapi_server import util


async def get_rankings(request: web.Request, year, week=None, season_type=None) -> web.Response:
    """Historical polls and rankings

    Poll rankings

    :param year: Year/season filter for games
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str

    """
    return web.Response(status=200)
