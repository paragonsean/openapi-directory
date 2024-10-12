from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcitymatch200_response import Getcitymatch200Response
from openapi_server import util


async def getcitymatch(request: web.Request, license, city) -> web.Response:
    """Gets a similarity key for matching purposes for city name data

    Gets a similarity key for matching purposes for city name data.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param city: City name from which to generate similarity key
    :type city: str

    """
    return web.Response(status=200)
