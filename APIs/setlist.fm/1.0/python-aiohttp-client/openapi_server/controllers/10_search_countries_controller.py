from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_countries import JsonCountries
from openapi_server import util


async def resource10_search_countries_get_countries_get(request: web.Request, ) -> web.Response:
    """Get a complete list of all supported countries.

    Get a complete list of all supported countries.


    """
    return web.Response(status=200)
