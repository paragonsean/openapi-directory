from typing import List, Dict
from aiohttp import web

from openapi_server.models.getaddressmatch200_response import Getaddressmatch200Response
from openapi_server import util


async def getaddressmatch(request: web.Request, license, address) -> web.Response:
    """Gets a similarity key for matching purposes for address data

    Gets a similarity key for matching purposes for street address data 

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param address: Address from which to generate similarity key
    :type address: str

    """
    return web.Response(status=200)
