from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def filmography_search_read(request: web.Request, movie_title) -> web.Response:
    """Return filmography search result

    Return filmography search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies * You can use both Amharic or English charset/font to search  For more details on how filmographies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param movie_title: 
    :type movie_title: str

    """
    return web.Response(status=200)


async def filmography_searchall_read(request: web.Request, param) -> web.Response:
    """Return filmography search result

    Return filmography search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or * filmography description (such as director, actor, producer, etc)  For more details on how filmographies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param param: 
    :type param: str

    """
    return web.Response(status=200)
