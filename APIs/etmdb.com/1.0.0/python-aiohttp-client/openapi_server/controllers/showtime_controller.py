from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def showtime_searchall_read(request: web.Request, param) -> web.Response:
    """Return showtime search result

    Return showtime search result  ### Response Class (Status 200) __{param}__ argument can be * show time or * day of the week [Mon&#x3D;1, Tue&#x3D;2, Wed&#x3D;3, Thu&#x3D;4, Fri&#x3D;5, Sat&#x3D;6, Sun&#x3D;7]  For more details about showtime, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

    :param param: 
    :type param: str

    """
    return web.Response(status=200)
