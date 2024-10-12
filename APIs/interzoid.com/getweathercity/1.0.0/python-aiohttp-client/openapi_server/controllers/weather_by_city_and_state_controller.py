from typing import List, Dict
from aiohttp import web

from openapi_server.models.getweather200_response import Getweather200Response
from openapi_server import util


async def getweather(request: web.Request, license, city, state) -> web.Response:
    """Gets current weather information for a US city and state

    Use city and state to retrieve current US weather information.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param city: City for weather information
    :type city: str
    :param state: State for weather information
    :type state: str

    """
    return web.Response(status=200)
