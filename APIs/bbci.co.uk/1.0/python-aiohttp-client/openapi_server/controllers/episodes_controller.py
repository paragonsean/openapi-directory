from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_clips(request: web.Request, pid, rights, availability) -> web.Response:
    """Get Clips

    Get Clips

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)


async def get_episodes_by_category(request: web.Request, category, lang, rights, availability, page, per_page, sort=None) -> web.Response:
    """List all the episodes for a category.

    Get the list of all the episodes for a given category in TV &amp; iPlayer.

    :param category: The category identifier to return results from.
    :type category: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param page: The page index.
    :type page: int
    :param per_page: The number of results to return.
    :type per_page: int
    :param sort: The sort order of the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_episodes_by_group(request: web.Request, pid, rights, page, per_page, initial_child_count, sort, sort_direction, availability, mixin=None) -> web.Response:
    """Get episodes by group, brand or series

    Get episodes by group, brand or series

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param page: The page index.
    :type page: int
    :param per_page: The number of results to return.
    :type per_page: int
    :param initial_child_count: The depth to return child entities.
    :type initial_child_count: int
    :param sort: The sort order of the results.
    :type sort: str
    :param sort_direction: Whether to sort ascending or descending
    :type sort_direction: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param mixin: Request additional data in the output
    :type mixin: List[str]

    """
    return web.Response(status=200)


async def get_episodes_by_parent_pid(request: web.Request, pid, rights, availability, initial_child_count) -> web.Response:
    """Child episodes for a given programme pid.

    Get the child episodes belonging to a given programme identifier.

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param initial_child_count: The depth to return child entities.
    :type initial_child_count: int

    """
    return web.Response(status=200)


async def get_onward_journey(request: web.Request, pid, rights, availability) -> web.Response:
    """Get Onward Journey

    Get Onward Journey (next programme)

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)


async def get_post_rolls(request: web.Request, pid, rights, availability) -> web.Response:
    """Get Follow-ups (post-rolls)

    Get Follow-ups (post-rolls)

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)


async def get_programme_by_pid(request: web.Request, pid, rights, availability, mixin=None) -> web.Response:
    """Episode for a given pid.

    Get the episode for a given episode identifier.

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param mixin: Request additional data in the output
    :type mixin: List[str]

    """
    return web.Response(status=200)


async def get_programme_recommendations(request: web.Request, pid, rights, availability, page, per_page) -> web.Response:
    """Get programme recommendations

    Get programme recommendations

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param page: The page index.
    :type page: int
    :param per_page: The number of results to return.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_programmes_popular(request: web.Request, rights, page, per_page, initial_child_count, sort, sort_direction, availability, mixin=None) -> web.Response:
    """Get programmes popular

    Get programmes popular

    :param rights: The rights group to limit results to.
    :type rights: str
    :param page: The page index.
    :type page: int
    :param per_page: The number of results to return.
    :type per_page: int
    :param initial_child_count: The depth to return child entities.
    :type initial_child_count: int
    :param sort: The sort order of the results.
    :type sort: str
    :param sort_direction: Whether to sort ascending or descending
    :type sort_direction: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param mixin: Request additional data in the output
    :type mixin: List[str]

    """
    return web.Response(status=200)


async def get_trailers_pre_rolls(request: web.Request, pid, rights, availability) -> web.Response:
    """Get Trailers (pre-rolls)

    Get Trailers (pre-rolls)

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)
