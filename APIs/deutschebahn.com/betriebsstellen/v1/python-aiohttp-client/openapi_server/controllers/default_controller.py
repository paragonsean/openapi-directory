from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.station import Station
from openapi_server import util


async def betriebsstellen_abbrev_get(request: web.Request, abbrev) -> web.Response:
    """Get information about a specific station or stop by abbrevation

    Get information about a specific station or stop by abbrevation

    :param abbrev: Station or stop abbrevation
    :type abbrev: str

    """
    return web.Response(status=200)


async def betriebsstellen_get(request: web.Request, name=None) -> web.Response:
    """Get information of stations matching a given text

    Get all station and stop infos

    :param name: A station name or part of it
    :type name: str

    """
    return web.Response(status=200)
