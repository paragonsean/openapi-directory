from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.live import Live
from openapi_server.models.match import Match
from openapi_server.models.match_idor_slug import MatchIDOrSlug
from openapi_server.models.match_opponents_object import MatchOpponentsObject
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server import util


async def get_lives(request: web.Request, page=None, per_page=None) -> web.Response:
    """List lives matches

    List currently running live matches, available from pandascore with live websocket data.

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    page = .from_dict(page)
    return web.Response(status=200)


async def get_matches(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """List matches

    List matches

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


async def get_matches_match_id_or_slug(request: web.Request, match_id_or_slug) -> web.Response:
    """Get a match

    Get a single match by ID or by slug

    :param match_id_or_slug: A match ID or slug
    :type match_id_or_slug: dict | bytes

    """
    match_id_or_slug = .from_dict(match_id_or_slug)
    return web.Response(status=200)


async def get_matches_match_id_or_slug_opponents(request: web.Request, match_id_or_slug) -> web.Response:
    """Get match&#39;s opponents

    List opponents (player or teams) for the given match

    :param match_id_or_slug: A match ID or slug
    :type match_id_or_slug: dict | bytes

    """
    match_id_or_slug = .from_dict(match_id_or_slug)
    return web.Response(status=200)


async def get_matches_past(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get past matches

    List past matches

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


async def get_matches_running(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get running matches

    List currently running matches

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


async def get_matches_upcoming(request: web.Request, filter=None, search=None, sort=None, range=None, page=None, per_page=None) -> web.Response:
    """Get upcoming matches

    List upcoming matches

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
