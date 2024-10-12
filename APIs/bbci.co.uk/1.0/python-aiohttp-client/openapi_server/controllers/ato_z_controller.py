from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_programmes_ato_z_search(request: web.Request, letter, rights, page, per_page, initial_child_count, sort, sort_direction, availability) -> web.Response:
    """Programmes by initial title character

    Get the Programmes whose title begins with the given initial character.

    :param letter: Letter to search by, a to z or the string &#39;0-9&#39;
    :type letter: str
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

    """
    return web.Response(status=200)
