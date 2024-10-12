from typing import List, Dict
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server import util


async def countries_list_get(request: web.Request, ) -> web.Response:
    """countries_list_get

    Lists the countries to which Handwritten can mail, their associated country ID and any costs


    """
    return web.Response(status=200)
