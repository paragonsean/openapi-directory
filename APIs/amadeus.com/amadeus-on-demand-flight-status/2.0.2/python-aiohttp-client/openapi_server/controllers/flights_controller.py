from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error401 import Error401
from openapi_server.models.error500 import Error500
from openapi_server.models.success_flights import SuccessFlights
from openapi_server import util


async def get_flights_status(request: web.Request, carrier_code, flight_number, scheduled_departure_date, operational_suffix=None) -> web.Response:
    """Retrieves a unique flight by search criteria.

    

    :param carrier_code: 2 to 3-character IATA carrier code ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). 
    :type carrier_code: str
    :param flight_number: 1 to 4-digit number of the flight. e.g. 4537
    :type flight_number: str
    :param scheduled_departure_date: scheduled departure date of the flight, local to the departure airport, format YYYY-MM-DD.
    :type scheduled_departure_date: str
    :param operational_suffix: 1-letter operational suffix assigned by the carrier to differentiate flight in case of delay changing the departure date e.g. A 
    :type operational_suffix: str

    """
    scheduled_departure_date = util.deserialize_date(scheduled_departure_date)
    return web.Response(status=200)
