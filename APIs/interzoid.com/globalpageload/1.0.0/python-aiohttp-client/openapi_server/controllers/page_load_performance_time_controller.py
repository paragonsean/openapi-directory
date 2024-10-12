from typing import List, Dict
from aiohttp import web

from openapi_server.models.globalpageload200_response import Globalpageload200Response
from openapi_server import util


async def globalpageload(request: web.Request, license, origin, url) -> web.Response:
    """Gets page load (or an API call) performance from a specified global geography such as Paris, Tokyo, Virginia, Mumbai, Frankfurt, London, Seoul, California, Sao Paolo, and many more.

    Gets page load performance from a specified geography 

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param origin: Geographic location to perform the measurement from (Paris, Hong Kong, Seoul, Mumbai, Sao Paolo, London, etc. see API home page for full list)
    :type origin: str
    :param url: specific URL to perform load test time
    :type url: str

    """
    return web.Response(status=200)
