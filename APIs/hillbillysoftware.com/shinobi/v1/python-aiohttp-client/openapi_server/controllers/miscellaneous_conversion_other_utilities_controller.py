from typing import List, Dict
from aiohttp import web

from openapi_server.models.imdb_id import ImdbID
from openapi_server import util


async def get_imd_bid_get_async(request: web.Request, access_token, query) -> web.Response:
    """Gets list of avaiable IMDB ids from Movies and TV Show databases, you can use those to query other end points that need ID&#39;s

    

    :param access_token: 
    :type access_token: str
    :param query: 
    :type query: str

    """
    return web.Response(status=200)
