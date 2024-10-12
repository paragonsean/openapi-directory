from typing import List, Dict
from aiohttp import web

from openapi_server.models.imdb_images import ImdbImages
from openapi_server import util


async def image_search_get(request: web.Request, accesstoken, query, strictmatch=None) -> web.Response:
    """Get images available for movie/tv show with passed query

    

    :param accesstoken: 
    :type accesstoken: str
    :param query: Name or part of name from Movie or Show
    :type query: str
    :param strictmatch: 
    :type strictmatch: bool

    """
    return web.Response(status=200)


async def images_get(request: web.Request, access_token, imdb_id) -> web.Response:
    """Get images available for movie/tv show with passed imdbID

    

    :param access_token: 
    :type access_token: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)
