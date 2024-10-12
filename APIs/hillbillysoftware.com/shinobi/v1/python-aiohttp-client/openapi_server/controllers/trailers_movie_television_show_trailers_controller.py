from typing import List, Dict
from aiohttp import web

from openapi_server.models.trailer import Trailer
from openapi_server.models.trailer_count import TrailerCount
from openapi_server import util


async def trailer_count_by_id_get(request: web.Request, access_token, imdb_id) -> web.Response:
    """Get trailer count for passed ID

    

    :param access_token: 
    :type access_token: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)


async def trailer_count_by_name_get(request: web.Request, access_token, name) -> web.Response:
    """Get trailer count for passed name (Movie title or TVShow name)

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def trailer_search_get(request: web.Request, access_token, phrase) -> web.Response:
    """Gets trailers by search phrase (limited to 10 records)

    

    :param access_token: 
    :type access_token: str
    :param phrase: Trailer you like to search for
    :type phrase: str

    """
    return web.Response(status=200)


async def trailersby_id_get(request: web.Request, access_token, imdb_id) -> web.Response:
    """Get Trailers for passed imdbID

    

    :param access_token: 
    :type access_token: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)
