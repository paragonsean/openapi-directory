from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def current_movie_data_csv_get(request: web.Request, imd_bid) -> web.Response:
    """getMovieByIMDBid

    Returns a movie using the films unique IMDB identifier

    :param imd_bid: IMDB ID of the movie to return
    :type imd_bid: str

    """
    return web.Response(status=200)


async def current_movie_data_csv_get2(request: web.Request, movie_year) -> web.Response:
    """getMovieByYear

    Returns a movie based on the year of its release

    :param movie_year: Release year of the movies to return
    :type movie_year: str

    """
    return web.Response(status=200)
