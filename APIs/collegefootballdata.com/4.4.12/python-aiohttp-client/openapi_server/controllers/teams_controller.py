from typing import List, Dict
from aiohttp import web

from openapi_server.models.player import Player
from openapi_server.models.team import Team
from openapi_server.models.team_matchup import TeamMatchup
from openapi_server.models.team_talent import TeamTalent
from openapi_server import util


async def get_fbs_teams(request: web.Request, year=None) -> web.Response:
    """FBS team list

    Information on major division teams

    :param year: Year filter
    :type year: int

    """
    return web.Response(status=200)


async def get_roster(request: web.Request, team=None, year=None) -> web.Response:
    """Team rosters

    Roster data

    :param team: Team name
    :type team: str
    :param year: Season year
    :type year: int

    """
    return web.Response(status=200)


async def get_talent(request: web.Request, year=None) -> web.Response:
    """Team talent composite rankings

    Team talent composite

    :param year: Year filter
    :type year: int

    """
    return web.Response(status=200)


async def get_team_matchup(request: web.Request, team1, team2, min_year=None, max_year=None) -> web.Response:
    """Team matchup history

    Matchup history

    :param team1: First team
    :type team1: str
    :param team2: Second team
    :type team2: str
    :param min_year: Minimum year
    :type min_year: int
    :param max_year: Maximum year
    :type max_year: int

    """
    return web.Response(status=200)


async def get_teams(request: web.Request, conference=None) -> web.Response:
    """Team information

    Get team information

    :param conference: Conference abbreviation filter
    :type conference: str

    """
    return web.Response(status=200)
