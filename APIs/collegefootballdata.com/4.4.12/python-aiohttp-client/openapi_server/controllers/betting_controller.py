from typing import List, Dict
from aiohttp import web

from openapi_server.models.game_lines import GameLines
from openapi_server import util


async def get_lines(request: web.Request, game_id=None, year=None, week=None, season_type=None, team=None, home=None, away=None, conference=None) -> web.Response:
    """Betting lines

    Closing betting lines

    :param game_id: Game id filter
    :type game_id: int
    :param year: Year/season filter for games
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str
    :param team: Team
    :type team: str
    :param home: Home team filter
    :type home: str
    :param away: Away team filter
    :type away: str
    :param conference: Conference abbreviation filter
    :type conference: str

    """
    return web.Response(status=200)
