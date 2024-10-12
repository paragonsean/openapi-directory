from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.prediction import Prediction
from openapi_server import util


async def get_trip_purpose_prediction(request: web.Request, origin_location_code, destination_location_code, departure_date, return_date, search_date=None) -> web.Response:
    """Returns the forecast purpose of a trip

    

    :param origin_location_code: city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston
    :type origin_location_code: str
    :param destination_location_code: city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
    :type destination_location_code: str
    :param departure_date: the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25
    :type departure_date: str
    :param return_date: the date on which the traveler will depart from the destination to return to the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
    :type return_date: str
    :param search_date: the date on which the traveler is performing the search. If this parameter is not specified, current date will be used. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
    :type search_date: str

    """
    return web.Response(status=200)
