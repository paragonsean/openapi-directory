from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_dates import FlightDates
from openapi_server import util


async def get_flight_dates(request: web.Request, origin, destination, departure_date=None, one_way=None, duration=None, non_stop=None, max_price=None, view_by=None) -> web.Response:
    """Find the cheapest flight dates from an origin to a destination.

    

    :param origin: IATA code of the city from which the flight will depart  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MAD for Madrid 
    :type origin: str
    :param destination: IATA code of the city to which the flight is going.  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MUC for Munich 
    :type destination: str
    :param departure_date: the date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25. Ranges are specified with a comma and are inclusive
    :type departure_date: str
    :param one_way: if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered
    :type one_way: bool
    :param duration: exact duration or range of durations of the travel, in days. This parameter must not be set if oneWay is true. Ranges are specified with a comma and are inclusive, e.g. 2,8
    :type duration: str
    :param non_stop: if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered
    :type non_stop: bool
    :param max_price: defines the price limit for each offer returned. The value should be a positive number, without decimals
    :type max_price: int
    :param view_by: view the flight dates by DATE, DURATION, or WEEK. View by DATE (default when oneWay is true) to get the cheapest flight dates for every departure date in the given range. View by DURATION (default when oneWay is false) to get the cheapest flight dates for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight destination for every week in the given range of departure dates. Note that specifying a detailed view but large ranges may result in a huge number of flight dates being returned. For some very large numbers of flight dates, the API may refuse to provide a response
    :type view_by: str

    """
    return web.Response(status=200)
