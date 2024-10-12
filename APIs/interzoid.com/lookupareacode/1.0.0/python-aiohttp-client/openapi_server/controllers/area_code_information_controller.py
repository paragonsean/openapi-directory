from typing import List, Dict
from aiohttp import web

from openapi_server.models.getareacode200_response import Getareacode200Response
from openapi_server import util


async def getareacode(request: web.Request, license, areacode) -> web.Response:
    """Gets telephone area code information

    Gets telephone area code information for a given area code.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param areacode: Telephone area code to retrieve area code information
    :type areacode: str

    """
    return web.Response(status=200)
