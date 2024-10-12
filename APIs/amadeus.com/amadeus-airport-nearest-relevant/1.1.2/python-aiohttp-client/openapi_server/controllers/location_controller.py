from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server import util


async def get_nearest_relevant_airports(request: web.Request, latitude, longitude, radius=None, page_limit=None, page_offset=None, sort=None) -> web.Response:
    """Returns a list of relevant airports near to a given point.

    

    :param latitude: latitude location to be at the center of the search circle
    :type latitude: float
    :param longitude: longitude location to be at the center of the search circle
    :type longitude: float
    :param radius: radius of the search in Kilometer. Can be from 0 to 500, default value is 500 Km.
    :type radius: int
    :param page_limit: maximum items in one page
    :type page_limit: int
    :param page_offset: start index of the requested page
    :type page_offset: int
    :param sort: defines on which attribute the sorting will be done from the best option to the worst one: * **relevance** - Score value calculated based on distance and traffic analytics * **distance** - Distance from the location to the geo-code given in API request parameters * **analytics.flights.score** - Approximate score for ranking purposes calculated based on estimated number of flights from/to airport in one reference year (last year) * **analytics.travelers.score** - Approximate score for ranking purposes calculated based on estimated number of travelers in the airport for one reference year (last year) 
    :type sort: str

    """
    return web.Response(status=200)
