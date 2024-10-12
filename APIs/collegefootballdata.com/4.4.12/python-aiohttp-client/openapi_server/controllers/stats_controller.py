from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_game_stat import AdvancedGameStat
from openapi_server.models.advanced_season_stat import AdvancedSeasonStat
from openapi_server.models.team_season_stat import TeamSeasonStat
from openapi_server import util


async def get_advanced_team_game_stats(request: web.Request, year=None, week=None, team=None, opponent=None, exclude_garbage_time=None, season_type=None) -> web.Response:
    """Advanced team metrics by game

    Advanced team game stats

    :param year: Year filter (required if no team specified)
    :type year: int
    :param week: Week filter
    :type week: int
    :param team: Team filter (required if no year specified)
    :type team: str
    :param opponent: Opponent filter
    :type opponent: str
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool
    :param season_type: Season type filter (regular, postseason, or both)
    :type season_type: str

    """
    return web.Response(status=200)


async def get_advanced_team_season_stats(request: web.Request, year=None, team=None, exclude_garbage_time=None, start_week=None, end_week=None) -> web.Response:
    """Advanced team metrics by season

    Advanced team season stats

    :param year: Year filter (required if no team specified)
    :type year: int
    :param team: Team filter (required if no year specified)
    :type team: str
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool
    :param start_week: Starting week filter
    :type start_week: int
    :param end_week: Starting week filter
    :type end_week: int

    """
    return web.Response(status=200)


async def get_stat_categories(request: web.Request, ) -> web.Response:
    """Team stat categories

    Stat category list


    """
    return web.Response(status=200)


async def get_team_season_stats(request: web.Request, year=None, team=None, conference=None, start_week=None, end_week=None) -> web.Response:
    """Team statistics by season

    Team season stats

    :param year: Year filter (required if no team specified)
    :type year: int
    :param team: Team filter (required if no year specified)
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param start_week: Starting week filter
    :type start_week: int
    :param end_week: Starting week filter
    :type end_week: int

    """
    return web.Response(status=200)
