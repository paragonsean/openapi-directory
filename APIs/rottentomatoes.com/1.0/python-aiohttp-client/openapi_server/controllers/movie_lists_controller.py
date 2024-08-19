from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def box_office_movie_lists(request: web.Request, limit=None, country=None) -> web.Response:
    """box_office_movie_lists

    

    :param limit: Limits the number of movies returned
    :type limit: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def in_theaters_movie_lists(request: web.Request, page_limit=None, page=None, country=None) -> web.Response:
    """in_theaters_movie_lists

    

    :param page_limit: The amount of movies in theaters to show per page
    :type page_limit: str
    :param page: The selected page of in theaters movies
    :type page: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def opening_movies_movie_lists(request: web.Request, limit=None, country=None) -> web.Response:
    """opening_movies_movie_lists

    

    :param limit: Limits the number of opening movies returned
    :type limit: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def upcoming_movies_movie_lists(request: web.Request, page_limit=None, page=None, country=None) -> web.Response:
    """upcoming_movies_movie_lists

    

    :param page_limit: The amount of upcoming movies to show per page
    :type page_limit: str
    :param page: The selected page of upcoming movies
    :type page: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)
