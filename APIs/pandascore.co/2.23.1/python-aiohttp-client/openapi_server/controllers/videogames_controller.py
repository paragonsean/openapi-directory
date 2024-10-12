from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter_over_leagues import FilterOverLeagues
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.filter_over_short_videogame_versions import FilterOverShortVideogameVersions
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.league import League
from openapi_server.models.range_over_leagues import RangeOverLeagues
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.range_over_short_videogame_versions import RangeOverShortVideogameVersions
from openapi_server.models.search_over_leagues import SearchOverLeagues
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.search_over_short_videogame_versions import SearchOverShortVideogameVersions
from openapi_server.models.serie import Serie
from openapi_server.models.short_tournament import ShortTournament
from openapi_server.models.short_videogame_version import ShortVideogameVersion
from openapi_server.models.videogame import Videogame
from openapi_server.models.videogame_idor_slug import VideogameIDOrSlug
from openapi_server import util


async def get_videogames(request: web.Request, page=None, per_page=None) -> web.Response:
    """List videogames

    List videogames

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    page = .from_dict(page)
    return web.Response(status=200)


async def get_videogames_videogame_id_or_slug(request: web.Request, videogame_id_or_slug) -> web.Response:
    """Get a videogame

    Get a single videogame by ID or by slug

    :param videogame_id_or_slug: A videogame ID or slug
    :type videogame_id_or_slug: dict | bytes

    """
    videogame_id_or_slug = .from_dict(videogame_id_or_slug)
    return web.Response(status=200)


async def get_videogames_videogame_id_or_slug_leagues(request: web.Request, videogame_id_or_slug, search=None, sort=None, range=None, filter=None, page=None, per_page=None) -> web.Response:
    """get_videogames_videogame_id_or_slug_leagues

    

    :param videogame_id_or_slug: A videogame ID or slug
    :type videogame_id_or_slug: dict | bytes
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
    videogame_id_or_slug = .from_dict(videogame_id_or_slug)
    search = .from_dict(search)
    range = .from_dict(range)
    filter = .from_dict(filter)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_videogames_videogame_id_or_slug_series(request: web.Request, videogame_id_or_slug, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """List series for a videogame

    List series for the given videogame

    :param videogame_id_or_slug: A videogame ID or slug
    :type videogame_id_or_slug: dict | bytes
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
    videogame_id_or_slug = .from_dict(videogame_id_or_slug)
    filter = .from_dict(filter)
    search = .from_dict(search)
    range = .from_dict(range)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_videogames_videogame_id_or_slug_tournaments(request: web.Request, videogame_id_or_slug, filter=None, range=None, sort=None, search=None, page=None, per_page=None) -> web.Response:
    """Get tournaments for a videogame

    List tournaments of the given videogame

    :param videogame_id_or_slug: A videogame ID or slug
    :type videogame_id_or_slug: dict | bytes
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
    videogame_id_or_slug = .from_dict(videogame_id_or_slug)
    filter = .from_dict(filter)
    range = .from_dict(range)
    search = .from_dict(search)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_videogames_videogame_id_or_slug_versions(request: web.Request, videogame_id_or_slug, filter=None, range=None, sort=None, search=None, page=None, per_page=None) -> web.Response:
    """List videogame versions

    List available versions for a given videogame

    :param videogame_id_or_slug: A videogame ID or slug
    :type videogame_id_or_slug: dict | bytes
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
    videogame_id_or_slug = .from_dict(videogame_id_or_slug)
    filter = .from_dict(filter)
    range = .from_dict(range)
    search = .from_dict(search)
    page = .from_dict(page)
    return web.Response(status=200)
