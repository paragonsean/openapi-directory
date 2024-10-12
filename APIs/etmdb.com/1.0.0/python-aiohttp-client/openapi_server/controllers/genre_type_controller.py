from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def genre_type_search_read(request: web.Request, genre_description) -> web.Response:
    """Return genre type search result

    Return genre type search result  ### Response Class (Status 200)  * __{genre_description}__: Used as a key word to search genre types  For more details on how genre types are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param genre_description: 
    :type genre_description: str

    """
    return web.Response(status=200)
