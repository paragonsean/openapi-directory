from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def people_search_read(request: web.Request, user) -> web.Response:
    """Return cast search result

    Return cast search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username  For more details on how cast are listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date

    :param user: 
    :type user: str

    """
    return web.Response(status=200)
