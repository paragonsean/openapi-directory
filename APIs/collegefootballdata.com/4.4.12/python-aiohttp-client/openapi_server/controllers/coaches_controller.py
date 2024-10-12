from typing import List, Dict
from aiohttp import web

from openapi_server.models.coach import Coach
from openapi_server import util


async def get_coaches(request: web.Request, first_name=None, last_name=None, team=None, year=None, min_year=None, max_year=None) -> web.Response:
    """Coaching records and history

    Coaching history

    :param first_name: First name filter
    :type first_name: str
    :param last_name: Last name filter
    :type last_name: str
    :param team: Team name filter
    :type team: str
    :param year: Year filter
    :type year: int
    :param min_year: Minimum year filter (inclusive)
    :type min_year: int
    :param max_year: Maximum year filter (inclusive)
    :type max_year: int

    """
    return web.Response(status=200)
