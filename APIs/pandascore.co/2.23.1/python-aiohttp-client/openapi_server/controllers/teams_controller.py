from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter_over_leagues import FilterOverLeagues
from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.filter_over_teams import FilterOverTeams
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.league import League
from openapi_server.models.match import Match
from openapi_server.models.range_over_leagues import RangeOverLeagues
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.range_over_teams import RangeOverTeams
from openapi_server.models.search_over_leagues import SearchOverLeagues
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.search_over_teams import SearchOverTeams
from openapi_server.models.serie import Serie
from openapi_server.models.short_tournament import ShortTournament
from openapi_server.models.team import Team
from openapi_server.models.team_idor_slug import TeamIDOrSlug
from openapi_server import util


async def get_teams(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """List teams

    List teams

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
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_teams_team_id_or_slug(request: web.Request, team_id_or_slug) -> web.Response:
    """Get a team

    Get a single team by ID or by slug

    :param team_id_or_slug: A team ID or slug
    :type team_id_or_slug: dict | bytes

    """
    team_id_or_slug = .from_dict(team_id_or_slug)
    return web.Response(status=200)


async def get_teams_team_id_or_slug_leagues(request: web.Request, team_id_or_slug, search=None, sort=None, range=None, filter=None, page=None, per_page=None) -> web.Response:
    """Get leagues for a team

    List leagues in which the given team was part of

    :param team_id_or_slug: A team ID or slug
    :type team_id_or_slug: dict | bytes
    :param search: Options to search results
    :type search: dict | bytes
    :param sort: Options to sort results
    :type sort: List[str]
    :param range: Options to select results within ranges
    :type range: dict | bytes
    :param filter: Options to filter results. String fields are case sensitive
    :type filter: dict | bytes
    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    team_id_or_slug = .from_dict(team_id_or_slug)
    search = .from_dict(search)
    range = .from_dict(range)
    filter = .from_dict(filter)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_teams_team_id_or_slug_matches(request: web.Request, team_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get matches for team

    List matches for the given team

    :param team_id_or_slug: A team ID or slug
    :type team_id_or_slug: dict | bytes
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
    team_id_or_slug = .from_dict(team_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_teams_team_id_or_slug_series(request: web.Request, team_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get series for a team

    List series in which the given team was part of

    :param team_id_or_slug: A team ID or slug
    :type team_id_or_slug: dict | bytes
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
    team_id_or_slug = .from_dict(team_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_teams_team_id_or_slug_tournaments(request: web.Request, team_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get tournaments for a team

    List tournaments in which the given team was part of

    :param team_id_or_slug: A team ID or slug
    :type team_id_or_slug: dict | bytes
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
    team_id_or_slug = .from_dict(team_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)
