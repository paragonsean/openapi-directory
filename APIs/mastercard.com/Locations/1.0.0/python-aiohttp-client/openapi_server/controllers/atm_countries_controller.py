from typing import List, Dict
from aiohttp import web

from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def atms_v1_country_get(request: web.Request, ) -> web.Response:
    """Returns countries with valid ATM locations.

    Returns countries with valid ATM locations. 


    """
    return web.Response(status=200)
