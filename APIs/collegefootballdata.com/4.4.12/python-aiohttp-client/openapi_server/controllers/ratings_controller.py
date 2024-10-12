from typing import List, Dict
from aiohttp import web

from openapi_server.models.conference_sp_rating import ConferenceSPRating
from openapi_server.models.team_elo_rating import TeamEloRating
from openapi_server.models.team_sp_rating import TeamSPRating
from openapi_server.models.team_srs_rating import TeamSRSRating
from openapi_server import util


async def get_conference_sp_ratings(request: web.Request, year=None, conference=None) -> web.Response:
    """Historical SP+ ratings by conference

    Get average SP+ historical rating data by conference

    :param year: Season filter
    :type year: int
    :param conference: Conference abbreviation filter
    :type conference: str

    """
    return web.Response(status=200)


async def get_elo_ratings(request: web.Request, year=None, week=None, team=None, conference=None) -> web.Response:
    """Historical Elo ratings

    Elo rating data

    :param year: Season filter
    :type year: int
    :param week: Maximum week filter
    :type week: int
    :param team: Team filter
    :type team: str
    :param conference: Conference filter
    :type conference: str

    """
    return web.Response(status=200)


async def get_sp_ratings(request: web.Request, year=None, team=None) -> web.Response:
    """Historical SP+ ratings

    SP+ rating data

    :param year: Season filter (required if team not specified)
    :type year: int
    :param team: Team filter (required if year not specified)
    :type team: str

    """
    return web.Response(status=200)


async def get_srs_ratings(request: web.Request, year=None, team=None, conference=None) -> web.Response:
    """Historical SRS ratings

    SRS rating data (requires either a year or team specified)

    :param year: Season filter (required if team not specified)
    :type year: int
    :param team: Team filter (required if year not specified)
    :type team: str
    :param conference: Conference filter
    :type conference: str

    """
    return web.Response(status=200)
