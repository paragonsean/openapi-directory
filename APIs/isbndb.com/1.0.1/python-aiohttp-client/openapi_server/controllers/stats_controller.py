from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def stats_get(request: web.Request, ) -> web.Response:
    """Gets status on the ISBNDB Database

    Returns a status object about the ISBNDB database.


    """
    return web.Response(status=200)
