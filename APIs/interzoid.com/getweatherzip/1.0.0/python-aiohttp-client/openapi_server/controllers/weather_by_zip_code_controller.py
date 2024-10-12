from typing import List, Dict
from aiohttp import web

from openapi_server.models.getweatherzipcode200_response import Getweatherzipcode200Response
from openapi_server import util


async def getweatherzipcode(request: web.Request, license, zip) -> web.Response:
    """Gets current weather information for a US zip code

    Use a US zip code to retrieve current weather information

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param zip: Zip code for weather information
    :type zip: str

    """
    return web.Response(status=200)
