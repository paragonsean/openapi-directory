from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_players import FilterOverPlayers
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.match import Match
from openapi_server.models.player import Player
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_players import RangeOverPlayers
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_players import SearchOverPlayers
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.serie import Serie
from openapi_server.models.serie_idor_slug import SerieIDOrSlug
from openapi_server.models.short_tournament import ShortTournament
from openapi_server import util


async def get_series(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """List series

    List series

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


async def get_series_past(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get past series

    List past series

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


async def get_series_running(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get running series

    List currently running series

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


async def get_series_serie_id_or_slug(request: web.Request, serie_id_or_slug) -> web.Response:
    """Get a serie

    Get a single serie by ID or by slug

    :param serie_id_or_slug: A serie ID or slug
    :type serie_id_or_slug: dict | bytes

    """
    serie_id_or_slug = .from_dict(serie_id_or_slug)
    return web.Response(status=200)


async def get_series_serie_id_or_slug_matches(request: web.Request, serie_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get matches for a serie

    List matches of the given serie

    :param serie_id_or_slug: A serie ID or slug
    :type serie_id_or_slug: dict | bytes
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
    serie_id_or_slug = .from_dict(serie_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_series_serie_id_or_slug_matches_past(request: web.Request, serie_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get past matches for serie

    List past matches for the given serie

    :param serie_id_or_slug: A serie ID or slug
    :type serie_id_or_slug: dict | bytes
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
    serie_id_or_slug = .from_dict(serie_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_series_serie_id_or_slug_matches_running(request: web.Request, serie_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get running matches for serie

    List currently running matches for the given serie

    :param serie_id_or_slug: A serie ID or slug
    :type serie_id_or_slug: dict | bytes
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
    serie_id_or_slug = .from_dict(serie_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_series_serie_id_or_slug_matches_upcoming(request: web.Request, serie_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get upcoming matches for serie

    List upcoming matches for the given serie

    :param serie_id_or_slug: A serie ID or slug
    :type serie_id_or_slug: dict | bytes
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
    serie_id_or_slug = .from_dict(serie_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_series_serie_id_or_slug_players(request: web.Request, serie_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get players for a serie

    List players for the given serie

    :param serie_id_or_slug: Automatically added
    :type serie_id_or_slug: str
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


async def get_series_serie_id_or_slug_tournaments(request: web.Request, serie_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get tournaments for a serie

    List tournaments of the given serie

    :param serie_id_or_slug: A serie ID or slug
    :type serie_id_or_slug: dict | bytes
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
    serie_id_or_slug = .from_dict(serie_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_series_upcoming(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get upcoming series

    List upcoming series

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
