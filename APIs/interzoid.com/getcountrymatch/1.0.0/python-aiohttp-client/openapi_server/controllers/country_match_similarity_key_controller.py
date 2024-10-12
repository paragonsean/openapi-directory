from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcountrymatch200_response import Getcountrymatch200Response
from openapi_server import util


async def getcountrymatch(request: web.Request, license, country) -> web.Response:
    """Gets a similarity key for matching purposes for country name data

    Gets a similarity key to use for matching purposes for country name data

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param country: Country name from which to generate similarity key
    :type country: str

    """
    return web.Response(status=200)
