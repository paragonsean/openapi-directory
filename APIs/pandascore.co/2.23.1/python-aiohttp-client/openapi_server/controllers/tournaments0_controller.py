from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter_over_teams import FilterOverTeams
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.range_over_teams import RangeOverTeams
from openapi_server.models.search_over_teams import SearchOverTeams
from openapi_server.models.team import Team
from openapi_server.models.tournament_idor_slug import TournamentIDOrSlug
from openapi_server import util


async def get_tournaments_tournament_id_or_slug_teams(request: web.Request, tournament_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get teams for a tournament

    List teams for the given tournament

    :param tournament_id_or_slug: A tournament ID or slug
    :type tournament_id_or_slug: dict | bytes
    :param filter: Options to filter results. String fields are case sensitive
    :type filter: dict | bytes
    :param search: Options to search results
    :type search: dict | bytes
    :param sort: Options to sort results
    :type sort: List[str]
    :param range: Options to select results within ranges
    :type range: dict | bytes
    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    tournament_id_or_slug = .from_dict(tournament_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)
