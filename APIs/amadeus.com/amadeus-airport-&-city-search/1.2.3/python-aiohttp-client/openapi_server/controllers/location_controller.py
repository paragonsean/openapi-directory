from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server.models.success1 import Success1
from openapi_server import util


async def get_airport_city(request: web.Request, location_id) -> web.Response:
    """Returns a specific airports or cities based on its id.

    

    :param location_id: identifier of the location
    :type location_id: str

    """
    return web.Response(status=200)


async def get_airport_city_search(request: web.Request, sub_type, keyword, country_code=None, page_limit=None, page_offset=None, sort=None, view=None) -> web.Response:
    """Returns a list of airports and cities matching a given keyword.

    

    :param sub_type: sub type of the location (AIRPORT and/or CITY)
    :type sub_type: List[str]
    :param keyword: keyword that should represent the start of a word in a city or airport name or code.   Supported charaters are: A-Za-z0-9./:-&#39;()\&quot;
    :type keyword: str
    :param country_code: Country code of the location using [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US).
    :type country_code: str
    :param page_limit: maximum items in one page
    :type page_limit: int
    :param page_offset: start index of the requested page
    :type page_offset: int
    :param sort: defines on which attribute the sorting will be done: * analytics.travelers.score - sort by the number of travelers by airport or city, the airports and cities with the highest traffic are on top of the results 
    :type sort: str
    :param view: select the level of information of the reply: * LIGHT - Gives only the IATACode, name, detailedName, cityName and countryName * FULL - Adds on top of the LIGHT information the timeZoneOffset, geocode, detailed address and travelers.score default option is FULL 
    :type view: str

    """
    return web.Response(status=200)
