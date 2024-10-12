from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcountrystandard200_response import Getcountrystandard200Response
from openapi_server import util


async def getcountrystandard(request: web.Request, license, country) -> web.Response:
    """Gets country name standard

    Gets a pre-selected country name standard for various permutations of a given country name.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param country: Country name from which to retrieve the standardized version
    :type country: str

    """
    return web.Response(status=200)
