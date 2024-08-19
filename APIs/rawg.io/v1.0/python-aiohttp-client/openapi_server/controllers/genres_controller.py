from typing import List, Dict
from aiohttp import web

from openapi_server.models.genre_single import GenreSingle
from openapi_server.models.genres_list200_response import GenresList200Response
from openapi_server import util


async def genres_list(request: web.Request, ordering=None, page=None, page_size=None) -> web.Response:
    """Get a list of video game genres.

    

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def genres_read(request: web.Request, id) -> web.Response:
    """Get details of the genre.

    

    :param id: A unique integer value identifying this Genre.
    :type id: int

    """
    return web.Response(status=200)
