from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server import util


async def get_checkin_urls(request: web.Request, airline_code, language=None) -> web.Response:
    """Lists Check-in URLs.

    

    :param airline_code: Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)  [ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes) 
    :type airline_code: str
    :param language: Check-in page language with one of the following patterns &#39;languageCode&#39; (e.g. EN) or &#39;languageCode-IATAcountryCode&#39; (e.g. en-GB).   Default value is **en-GB** (used when required language is not available or when no value is specified). 
    :type language: str

    """
    return web.Response(status=200)
