from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcitystandard200_response import Getcitystandard200Response
from openapi_server import util


async def getcitystandard(request: web.Request, license, city) -> web.Response:
    """Gets a city name standard for US and international cities

    Gets a pre-selected city name standard for US and international cities for various permutations of a given city name.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param city: City name from which to retrieve the standardized version
    :type city: str

    """
    return web.Response(status=200)
