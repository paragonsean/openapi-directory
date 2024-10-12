from typing import List, Dict
from aiohttp import web

from openapi_server.models.getfullnamematch200_response import Getfullnamematch200Response
from openapi_server import util


async def getfullnamematch(request: web.Request, license, fullname) -> web.Response:
    """Gets a similarity key for matching purposes for full name data

    Gets a similarity key for matching purposes for full name data, where first and last name are part of the same field.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param fullname: Full name from which to generate similarity key
    :type fullname: str

    """
    return web.Response(status=200)
