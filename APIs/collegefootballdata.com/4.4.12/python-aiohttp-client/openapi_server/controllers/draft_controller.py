from typing import List, Dict
from aiohttp import web

from openapi_server.models.draft_pick import DraftPick
from openapi_server.models.draft_position import DraftPosition
from openapi_server.models.draft_team import DraftTeam
from openapi_server import util


async def get_draft_picks(request: web.Request, year=None, nfl_team=None, college=None, conference=None, position=None) -> web.Response:
    """List of NFL Draft picks

    List of NFL Draft picks

    :param year: Year filter
    :type year: int
    :param nfl_team: NFL team filter
    :type nfl_team: str
    :param college: Player college filter
    :type college: str
    :param conference: College confrence abbreviation filter
    :type conference: str
    :param position: NFL position filter
    :type position: str

    """
    return web.Response(status=200)


async def get_nfl_positions(request: web.Request, ) -> web.Response:
    """List of NFL positions

    List of NFL positions


    """
    return web.Response(status=200)


async def get_nfl_teams(request: web.Request, ) -> web.Response:
    """List of NFL teams

    List of NFL teams


    """
    return web.Response(status=200)
