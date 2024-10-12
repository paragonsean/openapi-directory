from typing import List, Dict
from aiohttp import web

from openapi_server.models.aliases import Aliases
from openapi_server import util


async def aliases_by_id_get(request: web.Request, access_token, imdb_id) -> web.Response:
    """Get known aliases for Movies or Television shows from passed imdbID

    

    :param access_token: 
    :type access_token: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)


async def aliases_get(request: web.Request, access_token, title) -> web.Response:
    """Get known aliases for Movies or Television shows

    

    :param access_token: 
    :type access_token: str
    :param title: Title of movie or television show
    :type title: str

    """
    return web.Response(status=200)
