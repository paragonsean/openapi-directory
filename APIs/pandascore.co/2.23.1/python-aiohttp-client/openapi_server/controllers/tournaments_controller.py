from typing import List, Dict
from aiohttp import web

from openapi_server.models.bracket import Bracket
from openapi_server.models.filter_over_brackets import FilterOverBrackets
from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_players import FilterOverPlayers
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.match import Match
from openapi_server.models.player import Player
from openapi_server.models.range_over_brackets import RangeOverBrackets
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_players import RangeOverPlayers
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.search_over_brackets import SearchOverBrackets
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_players import SearchOverPlayers
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.short_tournament import ShortTournament
from openapi_server.models.standing import Standing
from openapi_server.models.tournament import Tournament
from openapi_server.models.tournament_idor_slug import TournamentIDOrSlug
from openapi_server.models.tournament_rosters import TournamentRosters
from openapi_server import util


async def get_tournaments(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """List tournaments

    List tournaments

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


async def get_tournaments_past(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get past tournaments

    List past tournaments

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


async def get_tournaments_running(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get running tournaments

    List currently running tournaments

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


async def get_tournaments_tournament_id_or_slug(request: web.Request, tournament_id_or_slug) -> web.Response:
    """Get a tournament

    Get a single tournament by ID or by slug

    :param tournament_id_or_slug: A tournament ID or slug
    :type tournament_id_or_slug: dict | bytes

    """
    tournament_id_or_slug = .from_dict(tournament_id_or_slug)
    return web.Response(status=200)


async def get_tournaments_tournament_id_or_slug_brackets(request: web.Request, tournament_id_or_slug, filter=None, range=None, sort=None, search=None, page=None, per_page=None) -> web.Response:
    """Get a tournament&#39;s brackets

    Get the brackets of the given tournament

    :param tournament_id_or_slug: A tournament ID or slug
    :type tournament_id_or_slug: dict | bytes
    :param filter: Options to filter results. String fields are case sensitive
    :type filter: dict | bytes
    :param range: Options to select results within ranges
    :type range: dict | bytes
    :param sort: Options to sort results
    :type sort: List[str]
    :param search: Options to search results
    :type search: dict | bytes
    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    tournament_id_or_slug = .from_dict(tournament_id_or_slug)
    filter = .from_dict(filter)
    range = .from_dict(range)
    search = .from_dict(search)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_tournaments_tournament_id_or_slug_matches(request: web.Request, tournament_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get matches for tournament

    List matches for the given tournament

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


async def get_tournaments_tournament_id_or_slug_players(request: web.Request, tournament_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get players for a tournament

    List players for the given tournament

    :param tournament_id_or_slug: Automatically added
    :type tournament_id_or_slug: str
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


async def get_tournaments_tournament_id_or_slug_rosters(request: web.Request, tournament_id_or_slug) -> web.Response:
    """Get rosters for a tournament

    List participants (player or team) for a given tournament.

    :param tournament_id_or_slug: A tournament ID or slug
    :type tournament_id_or_slug: dict | bytes

    """
    tournament_id_or_slug = .from_dict(tournament_id_or_slug)
    return web.Response(status=200)


async def get_tournaments_tournament_id_or_slug_standings(request: web.Request, tournament_id_or_slug, page=None, per_page=None) -> web.Response:
    """Get tournament standings

    Get the current standings for a given tournament

    :param tournament_id_or_slug: A tournament ID or slug
    :type tournament_id_or_slug: dict | bytes
    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    tournament_id_or_slug = .from_dict(tournament_id_or_slug)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_tournaments_upcoming(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get upcoming tournaments

    List upcoming tournaments

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
