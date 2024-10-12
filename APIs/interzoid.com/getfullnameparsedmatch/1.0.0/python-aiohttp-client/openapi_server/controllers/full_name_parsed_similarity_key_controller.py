from typing import List, Dict
from aiohttp import web

from openapi_server.models.getfullnameparsedmatch200_response import Getfullnameparsedmatch200Response
from openapi_server import util


async def getfullnameparsedmatch(request: web.Request, license, firstname, lastname) -> web.Response:
    """Gets a similarity key for matching purposes for parsed full name data

    Gets a similarity key for matching purposes for parsed full name data, where the first name and last name are split into separate fields in the source data rather than combined.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param firstname: First name from which to generate similarity key
    :type firstname: str
    :param lastname: Last name from which to generate similarity key
    :type lastname: str

    """
    return web.Response(status=200)
