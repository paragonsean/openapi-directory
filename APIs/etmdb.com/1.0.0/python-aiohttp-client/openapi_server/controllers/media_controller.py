from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def media_search_read(request: web.Request, movie_title) -> web.Response:
    """Return movie media search result

    Return movie media search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search media for movies * You can use both Amharic or English charset/font to search  For more details on how media is listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param movie_title: 
    :type movie_title: str

    """
    return web.Response(status=200)


async def media_searchall_read(request: web.Request, user) -> web.Response:
    """Return cast media search result

    Return cast media search result  ### Response Class (Status 200) __{user}__ argument can be * artist first name * artist last name * artist username  For more details on how cast media is listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date

    :param user: 
    :type user: str

    """
    return web.Response(status=200)
