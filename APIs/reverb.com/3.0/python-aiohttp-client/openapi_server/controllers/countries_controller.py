from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def countries_get(request: web.Request, ) -> web.Response:
    """Retrieve a list of country codes with corresponding subregions

    Retrieve a list of country codes with corresponding subregions


    """
    return web.Response(status=200)
