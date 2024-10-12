from typing import List, Dict
from aiohttp import web

from openapi_server.models.getglobaltime200_response import Getglobaltime200Response
from openapi_server import util


async def getglobaltime(request: web.Request, license, locale) -> web.Response:
    """Gets the current time for a global locale

    Gets the current time for a global locale (city, state, region, or country such as Chicago, London, Paris, Seoul, Spain, Buenos Aires, Hawaii, Moscow, Tokyo, Hanoi, etc.)

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param locale: Geographic locale to get the current time for
    :type locale: str

    """
    return web.Response(status=200)
