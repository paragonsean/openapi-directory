from typing import List, Dict
from aiohttp import web

from openapi_server.models.getzipcodeinfo200_response import Getzipcodeinfo200Response
from openapi_server import util


async def getzipcodeinfo(request: web.Request, license, zip) -> web.Response:
    """Gets detailed zip code information

    For a given zip code, detailed information is returned, including city, state, latitude, longitude, area size, and various population demographics, including income, age, and presence of farming data.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param zip: Zip code to retrieve detailed information
    :type zip: str

    """
    return web.Response(status=200)
