from typing import List, Dict
from aiohttp import web

from openapi_server.models.drive import Drive
from openapi_server import util


async def get_drives(request: web.Request, year, season_type=None, week=None, team=None, offense=None, defense=None, conference=None, offense_conference=None, defense_conference=None, classification=None) -> web.Response:
    """Drive data and results

    Get game drives

    :param year: Year filter
    :type year: int
    :param season_type: Season type filter
    :type season_type: str
    :param week: Week filter
    :type week: int
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
    :param classification: Division classification filter (fbs/fcs/ii/iii)
    :type classification: str

    """
    return web.Response(status=200)
