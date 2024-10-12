from typing import List, Dict
from aiohttp import web

from openapi_server.models.position_group_recruiting_rating import PositionGroupRecruitingRating
from openapi_server.models.recruit import Recruit
from openapi_server.models.team_recruiting_rank import TeamRecruitingRank
from openapi_server import util


async def get_recruiting_groups(request: web.Request, start_year=None, end_year=None, team=None, conference=None) -> web.Response:
    """Recruit position group ratings

    Gets a list of aggregated statistics by team and position grouping

    :param start_year: Starting year
    :type start_year: int
    :param end_year: Ending year
    :type end_year: int
    :param team: Team filter
    :type team: str
    :param conference: conference filter
    :type conference: str

    """
    return web.Response(status=200)


async def get_recruiting_players(request: web.Request, year=None, classification=None, position=None, state=None, team=None) -> web.Response:
    """Player recruiting ratings and rankings

    Get player recruiting rankings and data. Requires either a year or team to be specified.

    :param year: Recruiting class year (required if team no specified)
    :type year: int
    :param classification: Type of recruit (HighSchool, JUCO, PrepSchool)
    :type classification: str
    :param position: Position abbreviation filter
    :type position: str
    :param state: State or province abbreviation filter
    :type state: str
    :param team: Committed team filter (required if year not specified)
    :type team: str

    """
    return web.Response(status=200)


async def get_recruiting_teams(request: web.Request, year=None, team=None) -> web.Response:
    """Team recruiting rankings and ratings

    Team recruiting rankings

    :param year: Recruiting class year
    :type year: int
    :param team: Team filter
    :type team: str

    """
    return web.Response(status=200)
