from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cinema_detail_search_read(request: web.Request, cinema_name) -> web.Response:
    """Return cinema details search result

    Return cinema details search result  ### Response Class (Status 200)  * __{cinema_name}__: Used as a key word to search cinemas,  For more details on how cinemas are listed [see here][ref]. [ref]: https://etmdb.com/en/cinema-list/-updated_date

    :param cinema_name: 
    :type cinema_name: str

    """
    return web.Response(status=200)
