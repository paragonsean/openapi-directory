from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_itinerary_price_metrics200_response import GetItineraryPriceMetrics200Response
from openapi_server import util


async def get_itinerary_price_metrics(request: web.Request, origin_iata_code, destination_iata_code, departure_date, currency_code=None, one_way=None) -> web.Response:
    """GET itinerary price metric

    

    :param origin_iata_code: airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), from which the traveler will depart 
    :type origin_iata_code: str
    :param destination_iata_code: airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), to which the traveler is going.
    :type destination_iata_code: str
    :param departure_date: The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format.
    :type departure_date: str
    :param currency_code: the preferred currency for display. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro
    :type currency_code: str
    :param one_way: true to get price metrics for a one way trip, false to get price metrics for a round trip
    :type one_way: bool

    """
    return web.Response(status=200)
