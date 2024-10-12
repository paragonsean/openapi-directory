from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcompanymatch200_response import Getcompanymatch200Response
from openapi_server import util


async def getcompanymatch(request: web.Request, license, company) -> web.Response:
    """Gets a similarity key for matching purposes for company name data

    Gets a similarity key for matching purposes for company name data

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param company: Company name from which to generate similarity key
    :type company: str

    """
    return web.Response(status=200)
