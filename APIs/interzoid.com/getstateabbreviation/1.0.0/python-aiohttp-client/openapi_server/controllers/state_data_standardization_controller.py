from typing import List, Dict
from aiohttp import web

from openapi_server.models.getstateabbreviation200_response import Getstateabbreviation200Response
from openapi_server import util


async def getstateabbreviation(request: web.Request, license, state) -> web.Response:
    """Gets a two-letter abbreviation for a state or province name data

    Gets a two-letter abbreviation for a state or province given a permutation of state or province data.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param state: State (or province) name from which to retrieve the two letter abbreviation.
    :type state: str

    """
    return web.Response(status=200)
