from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def company_credits_search_read(request: web.Request, movie_title) -> web.Response:
    """Return company credits search result

    Return company credits search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search company credits for the movie * You can use both Amharic or English charset/font to search  For more details on how company credits are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param movie_title: 
    :type movie_title: str

    """
    return web.Response(status=200)


async def company_credits_searchall_read(request: web.Request, param) -> web.Response:
    """Return company credits search result

    Return company credits search result  ### Response Class (Status 200) __{param}__ argument can be * company name * movie title or * company credit description (such as production, cinematography, etc)  For more details on how company credits are listed [see here][ref]. [ref]: https://etmdb.com/en/company-list/company_name

    :param param: 
    :type param: str

    """
    return web.Response(status=200)
