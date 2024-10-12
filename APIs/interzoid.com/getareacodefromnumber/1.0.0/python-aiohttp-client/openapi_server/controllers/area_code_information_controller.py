from typing import List, Dict
from aiohttp import web

from openapi_server.models.getareacodefromnumber200_response import Getareacodefromnumber200Response
from openapi_server import util


async def getareacodefromnumber(request: web.Request, license, number) -> web.Response:
    """Gets area code information from a telephone number

    The area code will be parsed out of a telephone number and used to retrieve information about the area code.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param number: Telephone number to retrieve area code information
    :type number: str

    """
    return web.Response(status=200)
