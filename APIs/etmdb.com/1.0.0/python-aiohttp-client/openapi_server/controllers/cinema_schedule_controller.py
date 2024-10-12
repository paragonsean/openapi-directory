from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cinema_schedule_search_read(request: web.Request, movie_title) -> web.Response:
    """Return cinema schedule search result

    Return cinema schedule search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie cast * You can use both Amharic or English charset/font to search  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param movie_title: 
    :type movie_title: str

    """
    return web.Response(status=200)


async def cinema_schedule_searchall_read(request: web.Request, param) -> web.Response:
    """Return cinema schedule search result

    Return cinema schedule search result  ### Response Class (Status 200) __{param}__ argument can be * movie title * cinema name * cinema hall name or * cinema technology  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param param: 
    :type param: str

    """
    return web.Response(status=200)
