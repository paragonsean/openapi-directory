from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.prediction import Prediction
from openapi_server import util


async def get_airport_on_time_prediction(request: web.Request, airport_code, _date) -> web.Response:
    """Returns a percentage of on-time flight departures from a given airport.

    

    :param airport_code: airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx), e.g. BOS for Boston
    :type airport_code: str
    :param _date: the date on which the traveler will depart from the give airport. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
    :type _date: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)
