from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def watchlist_search_read(request: web.Request, movie_title) -> web.Response:
    """Return watchlist search result

    Return watchlist search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies on watchlist * You can use both Amharic or English charset/font to search  For more details on how watchlist are listed [see here][ref]. [ref]: https://etmdb.com/en/movies/watchlist/id

    :param movie_title: 
    :type movie_title: str

    """
    return web.Response(status=200)


async def watchlist_searchall_read(request: web.Request, param) -> web.Response:
    """Return watchlist search result

    Return watchlist search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or  For more details on how watchlist are listed [see here][ref]. [ref]: https://etmdb.com/en/movies/watchlist/id

    :param param: 
    :type param: str

    """
    return web.Response(status=200)
