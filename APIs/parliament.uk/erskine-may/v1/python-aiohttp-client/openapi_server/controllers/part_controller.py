from typing import List, Dict
from aiohttp import web

from openapi_server.models.erskine_may_part import ErskineMayPart
from openapi_server import util


async def api_part_get(request: web.Request, ) -> web.Response:
    """Returns a list of all parts.

    


    """
    return web.Response(status=200)


async def api_part_part_number_get(request: web.Request, part_number) -> web.Response:
    """Returns a part by part number.

    

    :param part_number: Part by part number
    :type part_number: int

    """
    return web.Response(status=200)
