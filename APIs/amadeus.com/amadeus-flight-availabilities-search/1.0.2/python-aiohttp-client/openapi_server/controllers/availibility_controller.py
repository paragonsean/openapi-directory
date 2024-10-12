from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_flight_availabilities_query import GetFlightAvailabilitiesQuery
from openapi_server.models.success_availability import SuccessAvailability
from openapi_server import util


async def search_flight_availabilities(request: web.Request, x_http_method_override, get_flight_availabilities_body) -> web.Response:
    """Return list of Flight Availabilities based on posted searching criteria.

    

    :param x_http_method_override: the HTTP method to apply
    :type x_http_method_override: str
    :param get_flight_availabilities_body: list of criteria to retrieve a list of flight availabilities
    :type get_flight_availabilities_body: dict | bytes

    """
    get_flight_availabilities_body = GetFlightAvailabilitiesQuery.from_dict(get_flight_availabilities_body)
    return web.Response(status=200)
