from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_recommended_location200_response import GetRecommendedLocation200Response
from openapi_server import util


async def get_recommended_location(request: web.Request, city_codes, traveler_country_code=None, destination_country_codes=None) -> web.Response:
    """GET recommended destinations

    

    :param city_codes: City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx)
    :type city_codes: str
    :param traveler_country_code: Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US)
    :type traveler_country_code: str
    :param destination_country_codes: List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US)
    :type destination_country_codes: str

    """
    return web.Response(status=200)
