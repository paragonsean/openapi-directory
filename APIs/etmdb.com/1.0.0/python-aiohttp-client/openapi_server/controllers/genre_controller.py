from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def genre_search_read(request: web.Request, movie_title) -> web.Response:
    """Return movie genre search result

    Return movie genre search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie genres * You can use both Amharic or English charset/font to search  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param movie_title: 
    :type movie_title: str

    """
    return web.Response(status=200)


async def genre_searchall_read(request: web.Request, movie_genre_type) -> web.Response:
    """Return movie genre search result

    Return movie genre search result  ### Response Class (Status 200)  * __{movie_genre_type}__: Used as a key word to search movie genres  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param movie_genre_type: 
    :type movie_genre_type: str

    """
    return web.Response(status=200)
