from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def filmography_type_search_read(request: web.Request, filmography_description) -> web.Response:
    """Return filmography type search result

    Return filmography type search result  ### Response Class (Status 200)  * __{filmography_description}__: Used as a key word to search filmography types  For more details on how filmography types are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param filmography_description: 
    :type filmography_description: str

    """
    return web.Response(status=200)
