from typing import List, Dict
from aiohttp import web

from openapi_server.models.player_search_result import PlayerSearchResult
from openapi_server.models.player_season_stat import PlayerSeasonStat
from openapi_server.models.player_usage import PlayerUsage
from openapi_server.models.portal_player import PortalPlayer
from openapi_server.models.returning_production import ReturningProduction
from openapi_server import util


async def get_player_season_stats(request: web.Request, year, team=None, conference=None, start_week=None, end_week=None, season_type=None, category=None) -> web.Response:
    """Player stats by season

    Season player stats

    :param year: Year filter
    :type year: int
    :param team: Team filter
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param start_week: Start week filter
    :type start_week: int
    :param end_week: Start week filter
    :type end_week: int
    :param season_type: Season type filter (regular, postseason, or both)
    :type season_type: str
    :param category: Stat category filter (e.g. passing)
    :type category: str

    """
    return web.Response(status=200)


async def get_player_usage(request: web.Request, year, team=None, conference=None, position=None, player_id=None, exclude_garbage_time=None) -> web.Response:
    """Player usage metrics broken down by season

    Player usage metrics by season

    :param year: Year filter
    :type year: int
    :param team: Team filter
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param position: Position abbreviation filter
    :type position: str
    :param player_id: Player id filter
    :type player_id: int
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool

    """
    return web.Response(status=200)


async def get_returning_production(request: web.Request, year=None, team=None, conference=None) -> web.Response:
    """Team returning production metrics

    Returning production metrics

    :param year: Year filter
    :type year: int
    :param team: Team filter
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str

    """
    return web.Response(status=200)


async def get_transfer_portal(request: web.Request, year) -> web.Response:
    """Transfer portal by season

    Transfer portal by season

    :param year: Year filter
    :type year: int

    """
    return web.Response(status=200)


async def player_search(request: web.Request, search_term, position=None, team=None, year=None) -> web.Response:
    """Search for player information

    Search for players

    :param search_term: Term to search on
    :type search_term: str
    :param position: Position abbreviation filter
    :type position: str
    :param team: Team filter
    :type team: str
    :param year: Year filter
    :type year: int

    """
    return web.Response(status=200)
