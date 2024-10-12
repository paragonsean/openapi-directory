from typing import List, Dict
from aiohttp import web

from openapi_server.models.movie_information import MovieInformation
from openapi_server import util


async def movie_id_get(request: web.Request, accesstoken, imdb_id) -> web.Response:
    """movie_id_get

    

    :param accesstoken: 
    :type accesstoken: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)


async def movie_search_get_async(request: web.Request, access_token, query) -> web.Response:
    """Searches for movies, result set limited to 5 records

    

    :param access_token: 
    :type access_token: str
    :param query: 
    :type query: str

    """
    return web.Response(status=200)
