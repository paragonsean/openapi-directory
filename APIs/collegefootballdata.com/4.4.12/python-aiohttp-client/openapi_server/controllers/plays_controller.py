from typing import List, Dict
from aiohttp import web

from openapi_server.models.live_play_by_play import LivePlayByPlay
from openapi_server.models.play import Play
from openapi_server.models.play_stat import PlayStat
from openapi_server.models.play_stat_type import PlayStatType
from openapi_server.models.play_type import PlayType
from openapi_server import util


async def get_live_plays(request: web.Request, id) -> web.Response:
    """Live metrics and PBP (Patreon only)

    Get live metrics and PBP

    :param id: Game id
    :type id: int

    """
    return web.Response(status=200)


async def get_play_stat_types(request: web.Request, ) -> web.Response:
    """Types of player play stats

    Type of play stats


    """
    return web.Response(status=200)


async def get_play_stats(request: web.Request, year=None, week=None, team=None, game_id=None, athlete_id=None, stat_type_id=None, season_type=None, conference=None) -> web.Response:
    """Play stats by play

    Gets player stats associated by play (limit 1000)

    :param year: Year filter
    :type year: int
    :param week: Week filter
    :type week: int
    :param team: Team filter
    :type team: str
    :param game_id: gameId filter (from /games endpoint)
    :type game_id: int
    :param athlete_id: athleteId filter (from /roster endpoint)
    :type athlete_id: int
    :param stat_type_id: statTypeId filter (from /play/stat/types endpoint)
    :type stat_type_id: int
    :param season_type: regular, postseason, or both
    :type season_type: str
    :param conference: conference abbreviation filter
    :type conference: str

    """
    return web.Response(status=200)


async def get_play_types(request: web.Request, ) -> web.Response:
    """Play types

    Types of plays


    """
    return web.Response(status=200)


async def get_plays(request: web.Request, year, week, season_type=None, team=None, offense=None, defense=None, conference=None, offense_conference=None, defense_conference=None, play_type=None, classification=None) -> web.Response:
    """Play by play data

    Get play data and results

    :param year: Year filter
    :type year: int
    :param week: Week filter (required if team, offense, or defense, not specified)
    :type week: int
    :param season_type: Season type filter
    :type season_type: str
    :param team: Team filter
    :type team: str
    :param offense: Offensive team filter
    :type offense: str
    :param defense: Defensive team filter
    :type defense: str
    :param conference: Conference filter
    :type conference: str
    :param offense_conference: Offensive conference filter
    :type offense_conference: str
    :param defense_conference: Defensive conference filter
    :type defense_conference: str
    :param play_type: Play type filter
    :type play_type: int
    :param classification: Division classification filter (fbs/fcs/ii/iii)
    :type classification: str

    """
    return web.Response(status=200)
