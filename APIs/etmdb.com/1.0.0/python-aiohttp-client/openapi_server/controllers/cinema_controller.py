from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cinema_search_read(request: web.Request, id) -> web.Response:
    """Return cinema search result

    Return cinema search result  ### Response Class (Status 200)  * __{id}__: Used as a key to search cinemas,  For more details on how cinemas are listed [see here][ref]. [ref]: https://etmdb.com/en/cinema-list/-updated_date

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
