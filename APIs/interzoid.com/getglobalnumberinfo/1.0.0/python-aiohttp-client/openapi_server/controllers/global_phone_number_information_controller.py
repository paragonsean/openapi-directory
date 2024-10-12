from typing import List, Dict
from aiohttp import web

from openapi_server.models.getglobalnumberinfo200_response import Getglobalnumberinfo200Response
from openapi_server import util


async def getglobalnumberinfo(request: web.Request, license, intlnumber) -> web.Response:
    """Get demographic information for a global telephone number

    Get demographic information for a global telephone number, including city and country information, primary languages spoken, and mobile device identification.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param intlnumber: International number (with country code) to retrieve information for
    :type intlnumber: str

    """
    return web.Response(status=200)
