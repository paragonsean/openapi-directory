from typing import List, Dict
from aiohttp import web

from openapi_server.models.rating_item import RatingItem
from openapi_server import util


async def rating_by_name_get(request: web.Request, access_token, name) -> web.Response:
    """rating_by_name_get

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def rating_get(request: web.Request, access_token, imdb_id) -> web.Response:
    """Returns ratings from various resources(IMDB,Rotten Tomatoes, metaCritics, TVMaze etc) of passed IMDBid

    

    :param access_token: 
    :type access_token: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)
