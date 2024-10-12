from typing import List, Dict
from aiohttp import web

from openapi_server.models.deletion_incident import DeletionIncident
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.incident import Incident
from openapi_server.models.non_deletion_incident import NonDeletionIncident
from openapi_server.models.videogame_idor_slug import VideogameIDOrSlug
from openapi_server import util


async def get_additions(request: web.Request, page=None, per_page=None, type=None, since=None, videogame=None) -> web.Response:
    """List additions

    Get the latest additions.  This endpoint only shows unchanged objects.

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int
    :param type: Filter by result type(s)
    :type type: List[str]
    :param since: Filter out older results
    :type since: str
    :param videogame: Filter by videogame(s)
    :type videogame: list | bytes

    """
    page = .from_dict(page)
    since = util.deserialize_datetime(since)
    videogame = [VideogameIDOrSlug.from_dict(d) for d in videogame]
    return web.Response(status=200)


async def get_changes(request: web.Request, page=None, per_page=None, type=None, since=None, videogame=None) -> web.Response:
    """List changes

    Get the latest updates.  This endpoint only provides the latest change for an object. It does not keep track of previous changes.

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int
    :param type: Filter by result type(s)
    :type type: List[str]
    :param since: Filter out older results
    :type since: str
    :param videogame: Filter by videogame(s)
    :type videogame: list | bytes

    """
    page = .from_dict(page)
    since = util.deserialize_datetime(since)
    videogame = [VideogameIDOrSlug.from_dict(d) for d in videogame]
    return web.Response(status=200)


async def get_deletions(request: web.Request, page=None, per_page=None, type=None, since=None, videogame=None) -> web.Response:
    """List deletions

    Get the latest deleted documents

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int
    :param type: Filter by result type(s)
    :type type: List[str]
    :param since: Filter out older results
    :type since: str
    :param videogame: Filter by videogame(s)
    :type videogame: list | bytes

    """
    page = .from_dict(page)
    since = util.deserialize_datetime(since)
    videogame = [VideogameIDOrSlug.from_dict(d) for d in videogame]
    return web.Response(status=200)


async def get_incidents(request: web.Request, page=None, per_page=None, type=None, since=None, videogame=None) -> web.Response:
    """List changes, additions and deletions

     Get the latest updates and additions.  This endpoint only provides the latest incident for an object. It does not keep track of previous incidents.

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int
    :param type: Filter by result type(s)
    :type type: List[str]
    :param since: Filter out older results
    :type since: str
    :param videogame: Filter by videogame(s)
    :type videogame: list | bytes

    """
    page = .from_dict(page)
    since = util.deserialize_datetime(since)
    videogame = [VideogameIDOrSlug.from_dict(d) for d in videogame]
    return web.Response(status=200)
