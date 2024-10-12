from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_destinations import FlightDestinations
from openapi_server import util


async def get_flight_destinations(request: web.Request, origin, departure_date=None, one_way=None, duration=None, non_stop=None, max_price=None, view_by=None) -> web.Response:
    """Find the cheapest destinations where you can fly to.

    

    :param origin: IATA code of the city from which the flight will depart  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MAD for Madrid 
    :type origin: str
    :param departure_date: The date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25.   Ranges are specified with a comma and are inclusive  Departure date can not be more than 180 days in the future. 
    :type departure_date: str
    :param one_way: if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered
    :type one_way: bool
    :param duration: Exact duration or range of durations of the travel, in days.  This parameter must not be set if oneWay is true.   Ranges are specified with a comma and are inclusive, e.g. 2,8  Duration can not be lower than 1 days or higher than 15 days 
    :type duration: str
    :param non_stop: if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered
    :type non_stop: bool
    :param max_price: defines the price limit for each offer returned. The value should be a positive number, without decimals
    :type max_price: int
    :param view_by: view the flight destinations by DATE, DESTINATION, DURATION, WEEK, or COUNTRY. View by DATE (default when oneWay is true) to get the cheapest flight destination for every departure date in the given range. View by DURATION (default when oneWay is false) to get the cheapest flight destination for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight destination for every week in the given range of departure dates. View by COUNTRY to get the cheapest flight destination by country. Note that specifying a detailed view but large ranges may result in a huge number of flight destinations being returned. For some very large numbers of flight destinations, the API may refuse to provide a response
    :type view_by: str

    """
    return web.Response(status=200)
